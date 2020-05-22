### list all available namespaces that has at least one metric

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
                            'Stat':'Average',
                            'Period': 480
                        },
                    },
                ],
                StartTime=datetime(2020, 5, 1),
                EndTime=datetime(2020,5,22),
                ScanBy='TimestampDescending',
                MaxDatapoints=1
            )
            print(response)
except Exception as e:
    print(e)