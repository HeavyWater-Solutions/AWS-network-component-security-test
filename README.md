# HeavyWater Machine Learning Problem

### Purpose


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
2. cft_name :  Name of the cft created in the previous step.
3. keypair_name : Name of .pem file.


### Problem Statement


### Your Mission



### Measurement Criteria



