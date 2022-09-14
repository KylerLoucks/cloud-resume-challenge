import json
import boto3
# import requests
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):

    table = dynamodb.Table('cloud-resume-challenge')
    dynamodbResponse = table.update_item(Key={"ID": "viewers"},
    UpdateExpression='ADD Clicks :inc', # ADD will create an entry called 'viewers' if there isn't any, and update one if there is with the Clicks amount.
    ExpressionAttributeValues={':inc':1},
    ReturnValues="UPDATED_NEW")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': "Table Updated Successfully"})
    }
