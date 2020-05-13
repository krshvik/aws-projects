import boto3
import os
import sys

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    for record in event['Records']:
        print(record)
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        s3.Object(bucket,key).delete()