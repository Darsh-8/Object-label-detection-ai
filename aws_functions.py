import uuid
from datetime import datetime

import boto3
from boto3.dynamodb.conditions import Attr

from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION

BUCKET_NAME = "object-rekognition-images"
TABLE_NAME = "ImageLabels"

session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

s3 = session.client('s3')
rekognition = session.client('rekognition')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)


def upload_image_to_s3(file):
    unique_name = f"{uuid.uuid4()}.png"
    s3.upload_fileobj(file, BUCKET_NAME, unique_name)
    print(f"✅ Uploaded to S3: {unique_name}")
    return unique_name


def detect_labels(image_name):
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': image_name}},
        MaxLabels=10,
        MinConfidence=70
    )
    labels = [label['Name'] for label in response['Labels']]
    print(f"🔍 Rekognition labels for {image_name}: {labels}")
    return labels


def save_image_record(image_name, labels, manual_tags):
    timestamp = datetime.now().isoformat()
    table.put_item(Item={
        "ImageName": image_name,
        "Labels": labels,
        "ManualTags": manual_tags,
        "Timestamp": timestamp
    })
    print(
        f"📝 Saved to DynamoDB: {image_name} with tags {manual_tags} at {timestamp}")


def get_all_images():
    response = table.scan()
    items = response.get('Items', [])
    items.sort(key=lambda x: x.get('Timestamp', ''), reverse=True)
    return items


def search_images(query):
    response = table.scan(
        FilterExpression=Attr('Labels').contains(query) | Attr(
            'ManualTags').contains(query)
    )
    items = response.get('Items', [])
    items.sort(key=lambda x: x.get('Timestamp', ''), reverse=True)
    print(f"🔍 Search '{query}' found {len(items)} results")
    return items


def delete_image(image_name):
    s3.delete_object(Bucket=BUCKET_NAME, Key=image_name)
    print(f"🗑️ Deleted {image_name} from S3")
    table.delete_item(Key={'ImageName': image_name})
    print(f"🗑️ Deleted {image_name} record from DynamoDB")
