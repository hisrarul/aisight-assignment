## Task-2

#### Below is the list of resources created using cloudformation template
* ALBListener
* AutoscalingRole
* CloudwatchLogsGroup
* ContainerInstances
* EC2InstanceProfile
* EC2Role
* ECSALB
* ECSAutoScalingGroup
* ECSCluster
* ECSServiceRole
* ECSTG
* EcsSecurityGroup
* EcsSecurityGroupALBports
* EcsSecurityGroupHTTPinbound
* EcsSecurityGroupSSHinbound
* EcsServiceSecurityGroup
* EcsServiceSecurityGroupHTTPinbound
* GatewayAttachement
* InternetGateway
* PostsECSTG
* PostsListenerRule
* PostsService
* PostsServiceScalingTarget
* PostsTaskDefinition
* PublicRoute
* PublicRouteTable
* PublicSubnetOne
* PublicSubnetOneRouteTableAssociation
* PublicSubnetTwo
* PublicSubnetTwoRouteTableAssociation
* ServiceScalingTarget
* TaskDefinition
* ThreadDiscoveryService
* ThreadPrivateNamespace
* ThreadService
* ThreadsListenerRule
* UsersECSTG
* UsersListenerRule
* UsersService
* UsersServiceScalingTarget
* UsersTaskDefinition
* VPC

#### Build the docker images
```bash
docker build -t hisrarul/posts ./services/posts
docker build -t hisrarul/users ./services/users
docker build -t hisrarul/threads ./services/threads
```

#### Deploy the cloudformation stack
```bash
STACK_NAME='aisight-assignment'
REGION='ap-south-1'

aws cloudformation deploy \
   --template-file cf-ecs.yml \
   --region ${REGION} \
   --stack-name ${STACK_NAME} \
   --capabilities CAPABILITY_NAMED_IAM
```
