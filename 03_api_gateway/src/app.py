import json
import boto3

def getUsers(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def postUser(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getAdmins(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
