
brew install docker-machine

aws ec2 describe-vpcs

(venv) rcox15 ~/Code/flask-demo $ docker-machine create --driver amazonec2 --amazonec2-open-port 8000 --amazonec2-region eu-west-1 --amazonec2-zone a --amazonec2-vpc-id vpc-56a6c330 --amazonec2-instance-type t2.micro flask-demo

docker-machine create --driver amazonec2 --amazonec2-region eu-west-2 --amazonec2-instance-type t2.micro --amazonec2-open-port 80 flask-demo

eval $(docker-machine env flask-demo)

docker-compose up --build app

curl http://$(docker-machine ip flask-demo):5000

$(aws ec2 describe-vpcs --query 'Vpcs[0].VpcId' --output text)


# Flask Demo

A simple flask demo app deployed into an ubuntu 14.04 docker container, fronted with an nginx container.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine using Docker for development and testing purposes. See deployment for notes on how to deploy the project on AWS.

### Prerequisites

You will need an AWS account with credentials set up in ~/.aws/credentials as per https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html

Assuming you are working on a Mac;

- Download and install docker for mac from here:
https://store.docker.com/editions/community/docker-ce-desktop-mac

- Set up Brew
https://brew.sh/

- Install the AWS cli
`brew install awscli`

### Installing

In order to run the local development environment

- Build and start the Docker containers
`docker-compose up --build`

- You can reach the app in a browser at
`http://localhost`

- Check the containers are running using `docker-compose ps`

```
russ@russ-mpb:~/Code/flask-demo$ docker-compose ps
       Name                     Command               State           Ports         
------------------------------------------------------------------------------------
flask-demo_app_1     /bin/sh -c python3 run.py  ...   Up      0.0.0.0:5000->5000/tcp
flask-demo_nginx_1   nginx -g daemon off;             Up      0.0.0.0:80->80/tcp    
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
