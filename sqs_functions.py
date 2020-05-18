import boto3
sqs = boto3.client('sqs')

## an error occurs if you try to create a queue with the same name without waiting 60 seconds after deleting it

try:
    queue_name = 'test-queue2'
    response = sqs.create_queue(QueueName=queue_name)
    print(response['QueueUrl'],response['ResponseMetadata']['HTTPStatusCode'])
    qurl= response['QueueUrl']
    response = sqs.delete_queue(QueueUrl=qurl)
    print(response)
except Exception as e:
    print(e)

