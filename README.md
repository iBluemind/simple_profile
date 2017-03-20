# Simple Profile

A demo Flask web application for AWS(Amazon Web Services) beginner.


## Dependencies

This project is based on:

* Python3
* Flask  
* PyMySQL
* SQLAlchemy

and use these:

* Alembic
* uWSGI
* NGINX
* Bower
* Docker


## Configuration

This application fetch the configurations from the shell environment variables.

The shell environment variables used on this app are like below.
 
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* FLASKS3_BUCKET_NAME
* MYSQL_HOST
* MYSQL_PORT
* MYSQL_USER
* MYSQL_PASSWORD
* MYSQL_DATABASE

Drop all database tables and create the database models like:

```sh
$ flask initdb
```

You can minify CSS files, Javascript files using following command:

```sh
$ flask build_compressed_assets
```

The static resources can be uploaded on Amazon S3 using below command:

```sh
$ flask upload_to_s3
```


## Development Environment

You can install the dependencies related with frontend and backend like:

```sh
$ bower install
$ pip install -r requirements.txt
```

Or simply, you can run ```scripts/install.sh``` like below:

```sh
$ scripts/install.sh
```

This application can be started with below command.  
Before you start this app, check the whether shell environment variables were set.

```sh
$ flask run
```


## Deployment

This app can be deployed with docker-compose or Amazon Elastic Beanstalk.  
You must provide a correct value to shell environment variables on docker-compose.yml file or Dockerrun.aws.json.


### Docker Compose
```sh
$ docker-compose up -d
```


### Amazon Elastic Beanstalk 
```sh
$ eb init
$ eb create
```


## TroubleShooting

* Can't execute ```flask``` CLI commands!

    Set the shell environment variable ```FLASK_APP``` like below:

    ```sh
    $ export FLASK_APP=`pwd`/run.py
    ```


## License

MIT
