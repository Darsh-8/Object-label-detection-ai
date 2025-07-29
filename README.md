# 📸 Object & Label Detection Dashboard

![Python Version](https://img.shields.io/badge/python-3.8+-blue) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A Flask-based web app to upload images, auto-detect objects and labels using AWS Rekognition, store metadata in DynamoDB, and explore results on a searchable dashboard.

## 🖼️ Screenshots

![Dashboard Screenshot](https://drive.google.com/uc?export=view&id=14JuLLgbpOFt4x07DPduIMPvF5u8pV_3C)

## 🌟 Features

*   Upload images and store in **AWS S3**
*   Auto-detect labels using **Rekognition**
*   Add manual tags for custom labeling
*   Store all metadata in **DynamoDB**
*   Search & filter images by labels or tags
*   Dashboard stats: total images, most common label, total manual tags
*   RESTful API for stats (`/api/stats`)

## 🛠️ Tech Stack

*   **Back-end:** Python, Flask
*   **Front-end:** HTML5, CSS3 (inline styling)
*   **Cloud:** AWS S3, Rekognition, DynamoDB
*   **Env Mgmt:** `python-dotenv`
*   **Deps:** `requirements.txt`

## 🔧 Prerequisites

*   Python 3.8+ installed
*   AWS account with S3, Rekognition & DynamoDB permissions
*   Configured AWS credentials via environment variables
*   An S3 bucket named `object-rekognition-images`
*   A DynamoDB table `ImageLabels` with `ImageName` as primary key

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Darsh-8/objectandlabeldetection.git
```

```bash
cd objectandlabeldetection
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
# On Windows: venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

**Create a `.env` file:**

```
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
AWS_DEFAULT_REGION=ap-south-1
```

## 🚀 Running the App

```bash
export FLASK_APP=app.py
```

```bash
export FLASK_ENV=development
```

```bash
flask run
```

**Or simply:**

```bash
python app.py
```

## 📂 Project Structure

```

object-label-detection-ai/
├── aws_handlers/
│   └── aws_functions.py       # AWS integration logic
├── app.py                     # Flask app runner
├── config.py                  # AWS keys and config
├── templates/
│   └── index.html             # Dashboard UI
├── requirements.txt
├── README.md
```

## 🔍 Usage Examples

*   Upload an image to auto-detect labels
*   Enter comma-separated manual tags
*   Search for images by label or tag
*   API: `GET /api/stats`

```json

{
  "total_images": 42,
  "most_common_label": "Person",
  "total_manual_tags": 17
}
```

## 🚫 No Live Deployment

This application is currently **not hosted online**. To use it, follow the setup steps and run it locally.

## ⚠️ Limitations

*   No video or batch uploads — only single image upload
*   No confidence threshold control for label filtering
*   Dashboard lacks pagination or delete functionality
*   Open access — no user authentication or roles

## 🗺️ Roadmap

*   Add pagination to dashboard
*   Enable threshold-based filtering for labels
*   Add image delete functionality
*   Introduce user authentication (login/signup)
*   Allow export of metadata (CSV or JSON)

## 🤝 Contributing

Pull requests, issues, and forks are welcome. Feel free to improve features or fix bugs by submitting a PR.

## 📄 License

Licensed under the MIT License. See `LICENSE` for more details.

- - -

Built with ❤️ by [Darsh Thakkar](https://github.com/Darsh-8) using Flask & AWS Rekognition.
