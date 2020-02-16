import boto3
from botocore.exceptions import ClientError
import logging


# Create an S3 bucket with name and optional region
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# List all buckets (the objects) owned by this user
def list_bucket_objects():
    s3_client = boto3.client('s3')
    return s3_client.list_buckets()['Buckets']

