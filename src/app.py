import json
import boto3

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = "mysteriousmeat.data"
FILE_NAME = "thirdPlant/pageData.json"

s3 = boto3.client('s3')

def lambda_handler(event, context):
    get_object_response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=FILE_NAME,
    )

    logger.info(get_object_response)
    logger.info("=============================")
    object_json = json.loads(get_object_response['Body'].read().decode("utf-8"))

    return {
        "statusCode": 200,
        "body": json.dumps(object_json)
    }

def yaya_lambda_handler(event, context):
    return {
        "statusCode": 201
    }

