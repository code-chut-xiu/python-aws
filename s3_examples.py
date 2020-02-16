import aws.s3 as s3

# Let's get your Amazon S3
# s3 = boto3.resource('s3')

# Display the S3 buckets
# for bucket in s3.buckets.all():
#    print(bucket.name)
buckets = s3.list_bucket_objects()
for bucket in buckets:
    print(bucket['Name'])
