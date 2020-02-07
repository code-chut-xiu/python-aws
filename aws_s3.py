import boto3
from botocore.exceptions import ClientError
import logging


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


# Let's get your Amazon S3
s3 = boto3.resource('s3')

# Display the S3 buckets
for bucket in s3.buckets.all():
    print(bucket.name)
