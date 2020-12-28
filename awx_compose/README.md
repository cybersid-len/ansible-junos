### Quick start
1. clone this repo
1. $ `cd this_directory`
1. $ `chmod 777 redis_socket`
1. $ `docker-compose up -d`
1. $ `docker-compose logs -f --tail=1`
1. $ `firewall-cmd --zone=public --permanent --add-port=8081/tcp` - now proxy container is able to talk to awx_web container 
with in the same docker host
1. $ http://ip-address:8081/ admin/password

### Docker stack customization
1. edit docker-compose.yml file

### Enabling TSL
* You have two options here:
    * using ssl-proxy-manager
    * using awx_web

###### using awx_web
1. uncomment `# ssl oprion` in `docker-compose.yml` file
1. $ `openssl genrsa -out server.key 2048`
1. $ `openssl rsa -in server.key -out server.key`
1. $ `openssl req -sha256 -new -key server.key -out server.csr -subj '/CN=awx.ortoscale.com'`
1. $ `openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt`
1. $ `cat server.key > server.pem`
1. $ `cat server.crt >> server.pem`
1. $ `cp server.pem /root/.ssh/server.pem`
1. $ `chmod 600 /root/.ssh/server.pem`
1. $ `docker-compose up -d`
1. $ `docker-compose logs -f --tail=1`
