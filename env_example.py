import os

# Main Settings

os.environ["SECRET_KEY"] = "Your secret key"
os.environ["DEBUG"] = "0" # 0 = False, 1 = True

# Audd.io API Key
os.environ["api_token"] = "Your api token"

# S3 Upload
os.environ["AWS_ACCESS_KEY_ID"] = 'Your AWS access key'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'Your AWS secret key'
os.environ["AWS_STORAGE_BUCKET_NAME"] = 'Your AWS bucket name'
os.environ["AWS_S3_REGION_NAME"] = 'Your AWS region'
