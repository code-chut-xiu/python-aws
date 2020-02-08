import aws.s3 as s3
import boto3

# Let's get your Amazon S3
#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#    print(bucket.name)

# For a multi-profile user, the following line will specify the profile to be used.
# If user has only one profile, skip this line since the default profile will be picked up.
boto3.setup_default_session(profile_name='mobtechdev')

# List all buckets that belong to a user (at specified profile)
buckets = s3.list_bucket_objects()
for bucket in buckets:
    print(bucket['Name'])
