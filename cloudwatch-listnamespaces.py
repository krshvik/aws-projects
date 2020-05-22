### list all available namespaces that has at least one metric
### list all metrics and metric data for a given namespace, shown for dyanmodb below 

import boto3
import urllib3
from datetime import datetime

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
    all_namespaces = ['AWS/DynamoDB']
    for n in all_namespaces:
        response = lam.list_metrics(Namespace=n)
        metrics = response['Metrics']
        for m in metrics:
            print(n,m, m['MetricName'],m['Dimensions'])
        # print(response)
            response = lam.get_metric_data(
                MetricDataQueries=[
                    {
                        'Id':'vikram',
                        'MetricStat': {
                            'Metric': {
                                'Namespace': n,
                                'MetricName': m['MetricName'],
                            },
                            'Stat':'Sum',
                            'Period': 480
                        },
                    },
                ],
                StartTime=datetime(2020, 5, 13),
                EndTime=datetime(2020,5,22),
                ScanBy='TimestampDescending',
                MaxDatapoints=100
            )
            print(response)
except Exception as e:
    print(e)