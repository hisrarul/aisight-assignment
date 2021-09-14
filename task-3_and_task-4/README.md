## Task-3

#### The directory contain following components:
+ Docker-compose file to run wordpress and mysql
+ Extended same docker-compose file to monitor wordpress site using prometheus, grafana
+ Added wordpress_exporter to expose wordpress container metrics
+ Prometheus scraping rules
+ Grafana username is `admin` and password is `foobar`.

#### Deploy wordpress in detach mode
```bash
docker-compose up -d
```

#### Run go application
```bash
git clone https://github.com/hisrarul/wordpress_exporter
go mod init wordpress_exporter
go mod tidy
go build
go mod vendor
go build
```