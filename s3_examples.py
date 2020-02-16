import aws.s3 as s3
import boto3

WORKING_PROFILE = 'training'
TEST_S3_BUCKET = 'test-simple-storage'
# Let's get your Amazon S3
# s3 = boto3.resource('s3')

# Display the S3 buckets
# for bucket in s3.buckets.all():
#    print(bucket.name)

# For a multi-profile user, the following line will specify the profile to be used.
# If user has only one profile, skip this line since the default profile will be picked up.
boto3.setup_default_session(profile_name=WORKING_PROFILE)

# List all buckets that belong to a user (at specified profile)
buckets = s3.list_bucket_objects()
for bucket in buckets:
    print(bucket['Name'])

if s3.create_bucket(TEST_S3_BUCKET) is True:
    for bucket in s3.list_bucket_objects():
        print(bucket['Name'])

if s3.delete_bucket(TEST_S3_BUCKET) is True:
    for bucket in s3.list_bucket_objects():
        print(bucket['Name'])
