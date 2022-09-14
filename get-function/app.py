import json
import boto3
# import requests
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    table = dynamodb.Table('cloud-resume-challenge')
    dynamodbResponse = table.get_item(Key={'ID': "viewers"})
    
    if 'Item' in dynamodbResponse:
        count = str(dynamodbResponse['Item']['Clicks'])

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': json.dumps({
                "count": count
            })
        }
