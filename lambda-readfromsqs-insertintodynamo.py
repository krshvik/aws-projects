import json
import boto3
import os 

## This lambda function is used to read messages from a Queue and insert them into a Dynamo DB table 

def lambda_handler(event, context):

    for record in event['Records']:
        payload=json.loads(record["body"])
        ticket_info = payload['Message']
        ticket_info = ticket_info.replace("'",'"')
        t = json.loads(ticket_info)
        print(t['ticket']['customer'])
        print(t['ticket']['no'])
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('tickets')
        table.put_item(Item = {'cname':t['ticket']['customer'],'no':t['ticket']['no']})
