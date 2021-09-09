## Task 1

#### Build Jenkins image
```bash
docker build -t hisrarul/jenkins:sep2021 -f Dockerfile-Jenkins .
```

#### RUN Jenkins
```bash
docker run -p 8090:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/var/jenkins_home hisrarul/jenkins:sep2021
```

#### Deploy to Kubernetes
+ Create pipeline job in Jenkins
+ Run a build
+ This will successfully deploy app on kubernetes cluster.