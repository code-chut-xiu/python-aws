import boto3
from botocore.exceptions import ClientError


def get_descriptions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)


def reboot_instance(instance_ids):
    ec2 = boto3.client('ec2')
    try:
        ec2.reboot_instances(InstanceIds=instance_ids, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            print("No permission to reboot instances.")
            raise

    try:
        response = ec2.reboot_instances(InstanceIds=instance_ids, DryRun=False)
        print('Success', response)
    except ClientError as e:
        print('Error', e)
