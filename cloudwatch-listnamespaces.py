### list all available namespaces that has at least one metric

import boto3
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try:
    all_namespaces = {}
    lam = boto3.client('cloudwatch',verify=False)
    response = lam.list_metrics()
    metrics = response['Metrics']
    for m in metrics:
        nm = m['Namespace']
        all_namespaces[nm] = 1
    print(list(all_namespaces))
except Exception as e:
    print(e)