### list all s3 buckets
### upload a file to s3 bucket

import boto3
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s3 = boto3.client('s3',verify=False)
response = s3.list_buckets()

bucks = response['Buckets']

if len(bucks) > 0:
    buck  = bucks[0]['Name']
    cdir = os.path.abspath(os.getcwd())
    print(cdir)
    f = os.path.join(cdir,'cb.jpg')
    ### upload a file
    print(f)
    s3 = boto3.resource('s3',verify=False)
    s3.meta.client.upload_file(f,buck,'cb2.jpg')
