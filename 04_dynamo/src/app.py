import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

tableName = os.environ.get('TABLE_NAME')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)

def showsPerMovie(event, context):
    print(json.dumps(event))
    movie_id = event["queryStringParameters"]["movie_id"]
    response = table.query(
        KeyConditionExpression=Key('pk').eq(movie_id)
    )
    items = response['Items']
    print(items)
    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }

def buyTicket(event, context):
    print(json.dumps(event))
    person = json.loads(event["body"])["person_id"]
    show = json.loads(event["body"])["show_id"]
    table.update_item(
        Key={
            'pk': show,
            'sk': person
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully updated database')
    }
    
def peoplePerMovie(event, context):
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
