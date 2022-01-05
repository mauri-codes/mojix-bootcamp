import json
import boto3

def lambda_handler(event, context):
    # s3 = boto3.client('s3')
    # buckets_object = s3.list_buckets()
    # for bucket in buckets_object['Buckets']:
    #     print(bucket['Name'])
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
