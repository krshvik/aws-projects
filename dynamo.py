import boto3
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


dynamo = boto3.client('dynamodb',region_name='us-east-2',verify=False)

try:
    dynamo.create_table(TableName='vikram-test',
        AttributeDefinitions = [
                               {
                                   'AttributeName': 'name',
                                   'AttributeType': 'S'
                               },
                           ],
        KeySchema=[
                  {
                 'AttributeName': 'name',
                 'KeyType': 'HASH'
                  },
        ],
        BillingMode='PROVISIONED' ,
        ProvisionedThroughput={
                              'ReadCapacityUnits': 1,
                              'WriteCapacityUnits': 1
                              },
    )
except Exception as e:
    print(e)

all_tables = dynamo.list_tables()['TableNames']

for t in all_tables:
    desc = dynamo.describe_table(TableName=t)
    rcpu = desc['Table']['ProvisionedThroughput']['ReadCapacityUnits']
    wcpu = desc['Table']['ProvisionedThroughput']['WriteCapacityUnits']
    size = desc['Table']['TableSizeBytes']
    cou = desc['Table']['ItemCount']

    backup = dynamo.list_backups(TableName=t)
    if len(backup['BackupSummaries']) > 0:
        bkups = backup['BackupSummaries']
        for b in bkups:
            print(b['BackupName'],' is ',b['BackupStatus'])



    print(t,'read capacity ', rcpu,'write capacity ',wcpu,'size in bytes ', size,'item count ',cou)


# print(response)