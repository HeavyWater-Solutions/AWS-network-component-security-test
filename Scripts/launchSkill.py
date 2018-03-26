import boto3
import time
import sys

urlMaster = sys.argv[1]
McftName = sys.argv[2] #'SkillCFT'

client = boto3.setup_default_session(region_name='us-east-1')
client = boto3.client('cloudformation')

def main():
    try: 
        response = client.create_stack(
            StackName=McftName,
            TemplateURL=urlMaster,
            Capabilities=['CAPABILITY_IAM'])
        while True:
            response = client.list_stacks(StackStatusFilter=['CREATE_COMPLETE'])
            summary = response['StackSummaries']
            for stack in summary:
                if stack['StackName'] == McftName:
                    print('stack already exists')
                    break
    except Exception as e:
        print e

if __name__ == '__main__':
    main()
