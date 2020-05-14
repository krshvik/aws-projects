import boto3
from datetime import datetime
from pytz import timezone
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
zone = 'US/Central'


iam = boto3.client('iam',verify=False)

print('USER List')
for user in iam.list_users()['Users']:
    u = user['CreateDate']
    print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(user['UserName'],user['UserId'], user['Arn'], user['CreateDate'].strftime(fmt) ))
    print('----------------')

print('ROLE List')

for role in iam.list_roles()['Roles']:
    print('name:',role['RoleName'])
    print('arn:',role['Arn'])
    print('policy document:',role['AssumeRolePolicyDocument']['Statement'])
    print("-----------------")
print('GROUP List')

for group in iam.list_groups()['Groups']:
    print(group)

# for policy in iam.list_policies()['Policies']:
#     print(policy)

users = iam.list_users()
user_list = []
for key in users['Users']:
    result = {}
    Policies = []
    Groups=[]

    result['userName']=key['UserName']
    List_of_Policies =  iam.list_user_policies(UserName=key['UserName'])

    result['Policies'] = List_of_Policies['PolicyNames']

    List_of_Groups =  iam.list_groups_for_user(UserName=key['UserName'])

    for Group in List_of_Groups['Groups']:
        Groups.append(Group['GroupName'])
    result['Groups'] = Groups

    List_of_MFA_Devices = iam.list_mfa_devices(UserName=key['UserName'])

    if not len(List_of_MFA_Devices['MFADevices']):
        result['isMFADeviceConfigured']=False
    else:
        result['isMFADeviceConfigured']=True
    user_list.append(result)

print(user_list)
