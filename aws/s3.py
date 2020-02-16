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
    # list_buckets method will return a response from the AWS S3 service.
    # Get the buckets via the 'Buckets' key.
    return s3_client.list_buckets()['Buckets']


def delete_bucket(bucket_name):
    s3_client = boto3.client('s3')

    try:
        s3_client.delete_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload_file_to_bucket(file_name, bucket_name, object_name=None):
    """"Upload a file to a S3 bucket
    """
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    result = True
    try:
        response = s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        result = False

    return result


def upload_file_object_to_bucket(file_name, bucket_name, object_name=None):
    s3_client = boto3.client('s3')
    result = True
    try:
        with open(file_name, 'rb') as f:
            response = s3_client.upload_fileobj(f, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        result = False

    return result


def download_file_from_bucket(file_name, bucket_name, object_name):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    result = True
    try:
        response = s3_client.download_file(bucket_name, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        result = False

    return result


def download_file_object_to_bucket(file_name, bucket_name, object_name=None):
    s3_client = boto3.client('s3')
    result = True
    try:
        with open(file_name, 'wb') as f:
            response = s3_client.download_fileobj(bucket_name, object_name, f)
    except ClientError as e:
        logging.error(e)
        result = False

    return result
