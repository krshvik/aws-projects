import json
import boto3

def lambda_handler(event, context):
    # TODO implement

    try:
        print(event['queryStringParameters']['qname'])
        a = event['queryStringParameters']['qname']
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('queue')
        table.put_item(Item = {'qname':a})

    except Exception as e:
        return {
            'statusCode':400,
            'body':json.dumps('invalid request')
        }
        
        
    return {
        'statusCode': 200,
        'body': 'queue created successfully'
    }

