import boto3
import json
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
lam = boto3.client('lambda',verify=False)
payload = {'a':22,'b':3311}
response = lam.invoke(FunctionName='addition',Payload=json.dumps(payload),InvocationType='RequestResponse')
print('http status code : ' ,response['StatusCode'])
ans = response['Payload']
ans_r = ans.read()
print(json.loads(ans_r)['body'])


## Definition of the lambda function

# import json
#
# def lambda_handler(event, context):
#     a = event['a']
#     b = event['b']
#     return {
#         'statusCode': 200,
#         'body': a+b
#     }
