import json
import boto3

BUCKET_NAME = "mysteriousmeat.data"
FILE_NAME = "thirdPlant/pageData.json"

def lambda_handler(event, context):
    # s3 = boto3.resource('s3')

    # content_object = s3.Object(BUCKET_NAME, FILE_NAME)
    # file_content = content_object.get()['Body'].read().decode('utf-8')
    # json_content = json.loads(file_content)
    # print(json_content['Details'])
    return {
        "statusCode": 200,
    }

