## Task-3

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