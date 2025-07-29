from collections import Counter

from flask import Flask, render_template, request, redirect, url_for, jsonify

from aws_functions import (
    upload_image_to_s3,
    detect_labels,
    save_image_record,
    get_all_images,
    search_images,
    delete_image
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        manual_tags = request.form.get("manual_tags", "").split(",")
        manual_tags = [tag.strip() for tag in manual_tags if tag.strip()]
        image_name = upload_image_to_s3(file)
        labels = detect_labels(image_name)
        save_image_record(image_name, labels, manual_tags)
        return redirect("/")

    query = request.args.get("search")
    if query:
        images = search_images(query)
    else:
        images = get_all_images()

    # Dashboard stats
    total_images = len(images)
    all_labels = [label for img in images for label in img.get('Labels', [])]
    most_common_label = Counter(all_labels).most_common(1)
    most_common_label = most_common_label[0][0] if most_common_label else "N/A"

    all_manual_tags = [tag for img in images for tag in
                       img.get('ManualTags', [])]
    total_manual_tags = len(set(all_manual_tags))

    return render_template(
        "index.html",
        images=images,
        total_images=total_images,
        most_common_label=most_common_label,
        total_manual_tags=total_manual_tags,
        BUCKET_NAME="object-rekognition-images",
        AWS_DEFAULT_REGION="ap-south-1"  # or your region
    )


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    if query:
        images = search_images(query)
    else:
        images = get_all_images()
    return render_template("index.html", images=images, query=query,
                           bucket_name="object-rekognition-images")


@app.route("/delete/<image_name>", methods=["POST"])
def delete(image_name):
    delete_image(image_name)
    return redirect(url_for("index"))


@app.route("/api/stats")
def api_stats():
    images = get_all_images()
    from collections import Counter
    total_images = len(images)
    all_labels = [label for img in images for label in img.get('Labels', [])]
    most_common_label = Counter(all_labels).most_common(1)
    most_common_label = most_common_label[0][0] if most_common_label else "N/A"
    all_manual_tags = [tag for img in images for tag in
                       img.get('ManualTags', [])]
    total_manual_tags = len(set(all_manual_tags))
    return jsonify({
        "total_images": total_images,
        "most_common_label": most_common_label,
        "total_manual_tags": total_manual_tags
    })


if __name__ == "__main__":
    app.run()
