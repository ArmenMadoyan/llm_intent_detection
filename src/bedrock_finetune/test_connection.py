import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))

import boto3

print("KEY:", os.getenv("AWS_ACCESS_KEY_ID"))  # debug

bedrock = boto3.client("bedrock", region_name="us-east-1")

response = bedrock.list_foundation_models()
print(response)
