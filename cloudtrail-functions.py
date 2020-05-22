### create and delete a topic in a given region

import boto3
ct = boto3.client('cloudtrail')

### trying to create topic with an existing name works fine even in the same region, without any issues

try:
    response = ct.lookup_events()
    print(response)
    events = response['Events']
    for e in events:
        print(e)
except Exception as e:
    print(e)