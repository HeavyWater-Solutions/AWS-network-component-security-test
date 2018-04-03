# HeavyWater Network Security Problem

### Purpose
To evaluate the candidates ability to learn AWS best practice of Building a Modular and Scalable Virtual Network Architecture with Amazon VPC.
Attached are the two cloud formations , one creates a VPC another deploys an EC2 in one one the subnets.

### Cloud formation templates (CFT)

> CFT/SkillCFT.json 

1. It is the cloud formation template creates seven layered infrastructure & 1 instance: HW-NAT. 
2. This template includes all the configurations of VPCs, Subnets, SecurityGroups, Inboud/Outbound Routing rules and so on.

> CFT/H2OServerApplication.json 

1. It is the cloud formation template that launches an EC2 instance and deploys H2O Web UI which is configured though the Application Load balancer. 
2. To be able to deploy this server some of the resources like VPC,Subnets created by SkillCFT are used.

### Scripts

##### Scripts/launchSkill.py 
Is used to launch the SKillCFT template.
See below how to execute the script using aws-cli

 >python Scripts/launchSkill.py template_url cft_name

1. template_url : S3 url where SkillCFT.json template is stored
>> Example: https://s3.amazonaws.com/bucketname/foldername/SkillCFT.json
2. cft_name :  Name of the stack you want to create


##### Scripts/launchH2O.py 

Is used to launch the H2OServerApplication template.
See below how to execute the script using aws-cli

>python Scripts/launchH2O.py template_url skill_cft_name keypair_name
1. template_url : S3 url where H2OServerApplication template is stored
>> Example: https://s3.amazonaws.com/bucketname/foldername/H2OServerApplication.json
2. skill_cft_name :  Name of the cft created in the previous step.
3. keypair_name : Name of .pem file.


### Problem Statement
Using the AWS quick start as reference :
>https://docs.aws.amazon.com/quickstart/latest/vpc/architecture.html

Improve the two CFT to satisfy the following security and resiliency features:

1. Least privilege control over your virtual networking environment, including selection of an IP address range, creation of subnets, and configuration of route tables and network gateways.
2. Implement H2O in four Availability Zones for high availability and disaster recovery.
3. Modify the subnets created by SkillCFT and place H2O in the appropriate subnet to allow for unique routing requirements.
4. Using network ACLs as firewalls to control inbound and outbound traffic at the subnet level.
5. Create Independent routing tables configured for every private subnet to control the flow of traffic within and outside the Amazon VPC.
6. Use highly available NAT gateways, where supported, instead of NAT instances.
7. Spare capacity for additional subnets, to support your environment as it grows or changes over time.
8. Includes VPC endpoints, which provide a secure, reliable connection to Amazon S3 without requiring an Internet gateway, a NAT device, or a virtual private gateway.


### Your Mission
Is to modify the provided CFTs , launch the CFTs in AWS and use trusted advisor to prove the additional security features added are in effect.



### Measurement Criteria

Create a penetration test to prove the security controls are in effect.

