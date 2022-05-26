import json
import boto3

# You can reference EFS files by including your local mount path, and then
# treat them like any other file. Local invokes may not work with this, however,
# as the file/folders may not be present in the container.
BUCKET_NAME = "mysteriousmeat.data"
FILE_NAME = "thirdPlant/pageData.json"

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    content_object = s3.Object(BUCKET_NAME, FILE_NAME)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    print(json_content['Details'])
    return json_content
