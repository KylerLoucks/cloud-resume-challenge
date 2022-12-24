import json
import boto3
# import requests
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    table = dynamodb.Table('cloud-resume-challenge')
    dynamodbResponse = table.get_item(Key={'ID': "viewers"})
    
    if 'Item' in dynamodbResponse:
        count = str(dynamodbResponse['Item']['Clicks'])
    else:
        count = "0"
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://www.example.com',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps({"count": count})
    }
