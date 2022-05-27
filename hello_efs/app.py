import json
import boto3

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = "mysteriousmeat.data"
FILE_NAME = "thirdPlant/pageData.json"

region = "us-east-2"
s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger.info("s3 client created.")
    # Retrieve the list of existing buckets
    response = s3.list_buckets()

    bucket_list = []

    # Output the bucket names
    logger.info('Existing buckets:')
    for bucket in response['Buckets']:
        bucket_list.append(bucket["Name"])
        logger.info(f'  {bucket["Name"]}')
    return {
        "statusCode": 200,
        "body": {
            "bucket_list": bucket_list
        }
    }

