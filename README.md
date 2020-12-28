# Ortoscale Monitoring System
## Description
This repo aims to deploy an OSM's component as a docker stacks.
* OMS components:
    * awx_compose
    * grafana-backend
    * grafana-frontend
    * nginx-proxy-namager
    * portainer-compose
    * etc
    
## Quick start
### Prepare docker host (ContOS 7):
1. $ `hostnamectl set-hostname oms-127`
1. $ `yum update -y && yum install bash-completion wget git nano`

### Install Docker
1. $ `curl -fsSL https://get.docker.com | bash`
1. $ `systemctl enable docker.service`
1. $ `systemctl start docker.service`
### Install docker compose [official docs](https://docs.docker.com/compose/install/)
See what is the latest version of docker compose [here](https://github.com/docker/compose/releases)
Pay attention at [get_docker-compose.sh](https://github.com/PrettySolution/get-scripts/blob/master/get_docker-compose.sh)
file to make sure you are going to install the latest version with the following step
1. $ `curl -fsSL https://raw.githubusercontent.com/PrettySolution/get-scripts/master/get_docker-compose.sh | bash` - install docker-compose
1. $ ` sudo curl -L https://raw.githubusercontent.com/docker/compose/1.27.4/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose`

## how to install an OMS component
### install awx_compose as a part of a customer setup (persolvo):
1. $ `mkdir /monitor/customers/persolvo/persolvo-awx -p`
1. $ `git clone https://github.com/PrettySolution/orto-compose-bluepints.git /monitor/orto-compose-bluepints/`
1. $ `cp -R /monitor/orto-compose-bluepints/awx_compose/* /monitor/customers/persolvo/persolvo-awx/`
1. $ `cd /monitor/customers/persolvo/persolvo-awx`
1. $ do what says docs `cat README.md`

### install nginx-proxy-manager as the system part:
1. $ `mkdir /monitor/system/system-nginx-proxy-manager -p`
1. $ `git clone https://github.com/PrettySolution/orto-compose-bluepints.git /monitor/orto-compose-bluepints/`
1. $ `cp -R /monitor/orto-compose-bluepints/nginx-proxy-manager/* /monitor/system/system-nginx-proxy-manager`
1. $ `cd /monitor/system/system-nginx-proxy-manager`
1. $ do what says docs `cat README.md`