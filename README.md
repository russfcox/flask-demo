# Flask Demo

A simple flask demo app deployed into an ubuntu 14.04 docker container, fronted with an nginx container.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine using Docker for development and testing purposes. See deployment for notes on how to deploy the project on AWS.

### Prerequisites

You will need an AWS account with credentials set up in ~/.aws/credentials as per https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html

Assuming you are working on a Mac, apologies to Windows or Linux users currently;

* Download and install docker for mac from here:
https://store.docker.com/editions/community/docker-ce-desktop-mac

* Set up Brew
https://brew.sh/

* Install the AWS cli
`brew install awscli`

* Install docker-machine for deployment
`brew install docker-machine`

## Installing

In order to run the local development environment

* Build and start the Docker containers
`docker-compose up -d --build`

* You can reach the app in a browser at
`http://localhost`

* Check the containers are running using `docker-compose ps`

```
russ@russ-mpb:~/Code/flask-demo$ docker-compose ps
       Name                     Command               State           Ports         
------------------------------------------------------------------------------------
flask-demo_app_1     /bin/sh -c python3 run.py  ...   Up      0.0.0.0:5000->5000/tcp
flask-demo_nginx_1   nginx -g daemon off;             Up      0.0.0.0:80->80/tcp    
```

* Logs can be fetched by running
`docker-compose logs`

* Shut down the stack
`docker-compose stop`

## Deployment

In order to deploy this into AWS

* Use docker-machine to provision a Docker host in AWS
`docker-machine create --driver amazonec2 --amazonec2-region eu-west-2 --amazonec2-instance-type t2.micro --amazonec2-open-port 80 flask-demo`

* Once docker-machine reports the machine is ready, configure your docker client to connect to it
`eval $(docker-machine env flask-demo)`

* Build and deploy the container images
`docker-compose up -d --build`

* Test the application is running correctly
`curl http://$(docker-machine ip flask-demo)` or `open http://$(docker-machine ip flask-demo)` to open it in a browser

## Production considerations
The Flask app in this demo is only for development purposes as the built-in server used is not suitable for production.
In order to make this production ready we could take steps along the lines of the following.

* Create a docker swarm, or ECS cluster in AWS to enable scalable hosting of containerised application, managed with an infrastructure orchestration tool such as Terraform.
* Use uWSGI in conjunction with nginx rather than Flask's built in server
* Store build docker images in a registry, tagged with appropriate versions
* Set up a CI/CD server such as CircleCI/Jenkins/AWS CodePipeline to handle automated build, test, and deployment of the container images on Git commit
* Configure autoscaling of the application containers and cluster to deal with traffic fluctuations
* Configure log shipping to a log aggregation service such as ELK / Loggly
* Configure monitoring of the application and cluster using tools such as Cloudwatch, Datadog, Newrelic, or AppDynamics
* Offload static assets to S3
* Configure caching - Cloudfront
