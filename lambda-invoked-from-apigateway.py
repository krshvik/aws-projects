import json

#### This lambda function is invoked from an API created using API Gateway; adds two numbers and returns the sum

def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(event['queryStringParameters']['a'])
    print(event['queryStringParameters']['b'])
    try:
        a = int(event['queryStringParameters']['a'])
        b = int(event['queryStringParameters']['b'])
    except Exception as e:
        return {
            'statusCode':400,
            'body':json.dumps('invalid request')
        }
        
        
    return {
        'statusCode': 200,
        'body': json.dumps(str(a+b))
    }
