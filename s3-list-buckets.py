### list all s3 buckets and their contents
### upload a file to s3 bucket - remove comments to upload a file

import boto3
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s3 = boto3.client('s3',verify=False)
response = s3.list_buckets()

bucks = response['Buckets']

if len(bucks) > 0:

    lenb = len(bucks)
    i = 0
    buck = ''
    while i < lenb:
        buck  = bucks[i]['Name']
        print(buck)
        response = s3.list_objects(Bucket=buck)
        contents = response['Contents']
        for c in contents:
            print(c['Key'],c['Size'],c['StorageClass'])
        i = i + 1
    # cdir = os.path.abspath(os.getcwd())
    # print(cdir)
    # f = os.path.join(cdir,'cb.jpg')
    # ### upload a file
    # print(f)
    # s3 = boto3.resource('s3',verify=False)
    # s3.meta.client.upload_file(f,buck,'cb2.jpg')
