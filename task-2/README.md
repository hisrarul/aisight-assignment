## Task-2

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
