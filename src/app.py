import json
import datetime
import boto3

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKET_NAME = "mysteriousmeat.data"
FILE_NAME = "pageData.json"

s3 = boto3.client('s3')

def lambda_handler(event, context):

    productName = event['queryStringParameters']['productName']

    s3PrefixAndFile = f'{productName}/{FILE_NAME}'

    get_object_response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=s3PrefixAndFile,
    )

    logger.info(get_object_response)
    logger.info("=============================")
    object_json = json.loads(get_object_response['Body'].read().decode("utf-8"))

    return {
        "statusCode": 200,
        "body": json.dumps(object_json)
    }

def yaya_lambda_handler(event, context):

    productName = event['queryStringParameters']['productName']
    s3PrefixAndFile = f'{productName}/{FILE_NAME}'

    timestamp = datetime.datetime.now().isoformat()
    message = event['headers']['message']

    get_object_response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=s3PrefixAndFile,
    )

    object_json = json.loads(get_object_response['Body'].read().decode("utf-8"))

    new_notes_list = list(object_json['pageData']['notes'])
    new_notes_list.append({"count": timestamp, "note": message})
    object_json['pageData']['notes'] = new_notes_list

    s3.put_object(
        Body=json.dumps(object_json),
        Bucket=BUCKET_NAME,
        Key=s3PrefixAndFile,
    )

    return {
        "statusCode": 201
    }

