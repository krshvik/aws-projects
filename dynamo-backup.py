### Creates back-up for a table
### Lists all backups for a given table
### Deletes all backups for a given table after a certain date

import boto3
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
dynamo = boto3.client('dynamodb',region_name='us-east-2',verify=False)
tname = 'queue'
try:
    response = dynamo.create_backup(TableName=tname,BackupName=tname+'_bkup')
    print(response)
except Exception as e:
    print(e)

try:
    response = dynamo.list_backups(TableName=tname,TimeRangeLowerBound=datetime(2019, 1, 1))
    backups = response['BackupSummaries']
    for b in backups:
        response =  dynamo.delete_backup(BackupArn=b['BackupArn'])
        print(b['BackupName'],b['BackupArn'],b['BackupType'],b['BackupSizeBytes'])
except Exception as e:
    print(e)

