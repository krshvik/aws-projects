### print network acl, subnet, vpc and security group
### print all internet gateways and route tables
import boto3
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ec2 = boto3.client('ec2',region_name='us-east-2',verify=False)



print('-------------------')

response = ec2.describe_network_acls()
nacls = response['NetworkAcls']
for n in nacls:
    for a in n['Associations']:
        print('Network ACL :',a)
        response = ec2.describe_subnets(Filters=[{'Name':'subnet-id','Values':[a['SubnetId']]}])
        snets = response['Subnets']
        for s in snets:
            print('Subnet :',s)
            response = ec2.describe_vpcs(Filters=[{'Name':'vpc-id','Values':[s['VpcId']]}])
            vpc = response['Vpcs']
            print('VPC :',vpc)
            response = ec2.describe_security_groups(Filters=[{'Name':'vpc-id','Values':[s['VpcId']]}])
            sgs = response['SecurityGroups']
            for sg in sgs:
                print('Security Group :',sg)
                print('--------------------------------------------------------------------------------------------')

print('-------------------')
response = ec2.describe_internet_gateways()
igs = response['InternetGateways']
for i in igs:
    print(i['InternetGatewayId'],'attached to VPC',json.dumps(i['Attachments'],indent=1))

print('-------------------')
response = ec2.describe_route_tables()
rts = response['RouteTables']
for r in rts:
    print(json.dumps(r,indent=1))
print('-------------------')
