# python-aws

# Create and activate virtualenv
virtualenv --system-site-packages -p python3 ./venv

source ./venv/bin/activate

# install the latest PIP
pip install --upgrade pip

# install the AWS Python SDK (https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
pip install boto3