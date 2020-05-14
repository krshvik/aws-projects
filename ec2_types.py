import boto3
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ec2 = boto3.client('ec2',region_name='us-east-2',verify=False)
ec2type = ec2.describe_instance_types()

for i in ec2type['InstanceTypes']:
    if i['FreeTierEligible']:
        print('free tier:' , i['InstanceType'],i['ProcessorInfo'],i['NetworkInfo'])
    else:
        print(i['InstanceType'],i['ProcessorInfo'],i['NetworkInfo'])
