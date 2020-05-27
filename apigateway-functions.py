### get all api names, along with stages and deployments
### get all available api keys/values, along with usage plans that are linked to specific apis

import boto3
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api = boto3.client('apigateway',verify=False)

response = api.get_rest_apis()
apis = response['items']
api_dict = {}

for a in apis:
    print(a['name'])
    id = a['id']
    api_dict[id] = a['name']
    response = api.get_rest_api(restApiId=id)

    stage = api.get_stages(restApiId=id)
    snames = stage['item']
    for s in snames:
        print(s['stageName'],' --> stage name')

    deps = api.get_deployments(restApiId=id)
    for d in deps['items']:
        print(d['id'],' --> deployment ID')

    print('-----------------------------------')

all_key = {}
response = api.get_api_keys()
keys = response['items']

for k in keys:
    id = k['id']
    plans = api.get_usage_plans(keyId=id)['items']
    for p in plans:
        pname = p['name']
        for apis in p['apiStages']:
            print("usage plan :" ,pname,"linked to stage",apis['stage'],"of api with name:",api_dict[apis['apiId']])
    # print(response)
    key = api.get_api_key(apiKey=id,includeValue=True)
    # print(key)
    all_key[id] = key['value']
print("all api keys (with value) :",all_key)