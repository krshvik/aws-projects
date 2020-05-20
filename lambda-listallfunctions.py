### list all lambda functions and concurrency

import boto3
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    lam = boto3.client('lambda',verify=False)
    response = lam.list_functions()
    functions = response['Functions']
    # print(functions)

    for f in functions:
        print(f['FunctionName'],f['FunctionArn'],f['Runtime'],f['MemorySize'])
        conc = lam.get_function_concurrency(FunctionName=f['FunctionName'])
        # print(conc)
        if 'ReservedConcurrentExecutions' in conc:
            print('concurrency is :',conc['ReservedConcurrentExecutions'])
        else:
            print(f['FunctionName'], ' has no reserved concurrent executions')
except Exception as e:
    print(e)