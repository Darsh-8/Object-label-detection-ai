# Object & Label Detection Dashboard

A Flask-based web application that lets you upload images, automatically detects objects & labels using AWS Rekognition, stores metadata in DynamoDB, and provides a searchable dashboard.

## 🌟 Features

- Image upload & storage in AWS S3
- Automated label detection via AWS Rekognition
- Manual tag input for custom metadata
- Metadata storage & retrieval in DynamoDB
- Search & filter by detected labels or manual tags
- Dashboard stats: total images, most common label, total manual tags
- RESTful API endpoint for stats (`/api/stats`)

## 🛠️ Tech Stack

- Back-end: Python, Flask
- Front-end: HTML5, CSS3 (in-template styling)
- AWS Services: S3, Rekognition, DynamoDB
- Dependencies managed via `requirements.txt`
- Environment variables via `python-dotenv`

## 🔧 Prerequisites

- Python 3.8+ installed
- AWS account with IAM user having S3, Rekognition & DynamoDB permissions
- Configured AWS credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`)
- An S3 bucket named `object-rekognition-images` (or adjust `BUCKET_NAME`)
- A DynamoDB table named `ImageLabels` with `ImageName` as primary key

## ⚙️ Installation & Setup

    python git clone https://github.com/Darsh-8/objectandlabeldetection.git
    python cd object-and-label-detection
    python python3 -m venv venv
    python source venv/bin/activate          <!-- on Windows: venv\Scripts\activate -->
    pip install -r requirements.txt

Create a `.env` file in the project root:

    AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
    AWS_DEFAULT_REGION=ap-south-1

## 🚀 Running the App

    export FLASK_APP=app.py
    export FLASK_ENV=development     <!-- optional: enables debug mode -->
    flask run                       <!-- by default runs on http://127.0.0.1:5000 -->

Or simply:

    python app.py

## 📂 Project Structure

    objectandlabeldetection/
    ├── app.py                  <!-- Main Flask application -->
    ├── aws_functions.py        <!-- S3, Rekognition & DynamoDB helpers -->
    ├── config.py               <!-- Loads AWS creds from .env -->
    └── templates/
        └── index.html          <!-- Dashboard & upload page -->
    requirements.txt            <!-- Python dependencies -->
    README.html                 <!-- This file -->

## 🔍 Usage Examples

- Upload an image via the dashboard to auto-detect labels.
- Enter comma-separated manual tags to augment Rekognition labels.
- Search images by label or manual tag using the search bar.
- View stats JSON: `GET /api/stats` returns:

      {
        "total_images": 42,
        "most_common_label": "Person",
        "total_manual_tags": 17
      }

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to fork the repo and submit a pull request.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

Built with ❤️ using Flask & AWS Rekognition
