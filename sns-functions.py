### create and delete a topic in a given region

import boto3
sns = boto3.client('sns',region_name='us-east-1')

### trying to create topic with an existing name works fine even in the same region, without any issues

try:
    response = sns.create_topic(Name='test-topic2')
    tarn = response['TopicArn']
    print('topic with arn :',tarn,' created')
    response = sns.delete_topic(TopicArn=tarn)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('topic deleted successfuly : ARN is ',tarn)
except Exception as e:
    print(e)