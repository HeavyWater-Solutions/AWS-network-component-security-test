import boto3
import time
import sys
import json
from multiprocessing.pool import ThreadPool


urls = sys.argv[1]
KeyPairName = sys.argv[3] #'testKP'
McftName = sys.argv[2] #'SkillCFT'
cftName = "H2OServerApplication"

parameters = []
BucketName = ''
VPCID = ""
Subnet = ""
Subnet2 = ""
Subnet3 = ""
Subnet4 = ""
Subnet5 = ""
Subnet6 = ""
Subnet7 = ""
Subnet8 = ""
SecurityGroup = ""
SecurityGroup2 = ""
SecurityGroup3 = ""
SecurityGroup4 = ""
SecurityGroup5 = ""
SecurityGroup6 = ""
RestApiRootResourceId = ""
RestApiId = ""
InstanceMinCount = "1"

client = boto3.setup_default_session(region_name='us-east-1')
client = boto3.client('cloudformation')
stacks = client.describe_stacks(StackName=McftName)
stack = stacks['Stacks']


for i, val in enumerate(stack):

    output = val['Outputs']
    for i1, val1 in enumerate(output):
        # print i1,val1
        if val1['OutputKey'] == 'VPCID':
            VPCID = val1['OutputValue']
        if val1['OutputKey'] == 'WEBAZ1subnet':
            Subnet = val1['OutputValue']
            #print Subnet
        if val1['OutputKey'] == 'ExternalELBAZ1subnet':
            Subnet2 = val1['OutputValue']
            #print Subnet2
        if val1['OutputKey'] == 'ExternalELBAZ2subnet':
            Subnet2_ = val1['OutputValue']
        if val1['OutputKey'] == 'WEBsecuritygroup':
            SecurityGroup = val1['OutputValue']
            #SecurityGroup = 'sg-8153c1f7'
            #print SecurityGroup
        if val1['OutputKey'] == 'ExternalELBsecuritygroup':
            SecurityGroup2 = val1['OutputValue']
            #SecurityGroup2 = 'sg-7ab9dd0c'
            #print SecurityGroup2

print VPCID
print Subnet
print Subnet2
print Subnet2_
print SecurityGroup
print SecurityGroup2



def my_CFT():
        try:
            response = client.create_stack(
                StackName=cftName,
                TemplateURL=urls,
                Capabilities=['CAPABILITY_IAM'],
                OnFailure='ROLLBACK',
                Parameters=[
                    {
                        'ParameterKey': 'VPC',
                        'ParameterValue': VPCID
                    }, 
                    {
                        'ParameterKey': 'KeyPairName',
                        'ParameterValue': KeyPairName
                    },
                    {
                        'ParameterKey': 'BucketName',
                        'ParameterValue': BucketName
                    },
                    {
                        'ParameterKey': 'ExternalELBsecuritygroup',
                        'ParameterValue': SecurityGroup2
                    },
                    {
                        'ParameterKey': 'ExternalELBAZ1subnet',
                        'ParameterValue': Subnet2
                    },
                    {
                        'ParameterKey': 'ExternalELBAZ2subnet',
                        'ParameterValue': Subnet2_
                    },
                    {
                        'ParameterKey': 'WEBAZ1subnet',
                        'ParameterValue': Subnet
                    },
                    {
                        'ParameterKey': 'WEBsecuritygroup',
                        'ParameterValue': SecurityGroup
                    }

                ], )
        except Exception:
            pass

my_CFT()
