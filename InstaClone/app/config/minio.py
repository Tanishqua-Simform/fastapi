import os
import boto3
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()

s3_client = boto3.client(
    's3',
    endpoint_url=os.getenv('MINIO_ENDPOINT_URL'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

MY_BUCKET = os.getenv('MY_BUCKET')

def upload(directory, filename):
    uid = uuid4()
    object_key = 'posts/'+ str(uid.int) + '_' + filename
    file_path = f'{directory}/{filename}'
    s3_client.upload_file(file_path, MY_BUCKET, object_key)
    image_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': MY_BUCKET, 'Key': object_key}
    )
    return image_url