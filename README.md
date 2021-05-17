# Money Management Dashboard

This app allows registered users to track their money transfers.

## Setup

#### With docker

Visit [docker](https://docs.docker.com/get-docker/) for installation instructions.

###### Build the docker image
```
docker build -t dashboard:latest .
```

###### Run the application
```
docker run --name dashboard -d -p 5000:5000 --rm dashboard:latest
```

Visit [localhost:5000](http://localhost:5000) in a browser

#### Without Docker

###### Initial Steps

* Clone repository
* `cd` to the project's root directory
* Run `python3 -m venv venv`
* Run `venv/bin/pip install -r requirements.txt`
* Run `source venv/bin/activate`

###### Setup your environment variables
In your root directory, create a `.env` file and add the following:

```
FLASK_APP=dashboard.py
SECRET_KEY=sekret
```

###### Tests and Execution
* Run `flask db upgrade`
* Run `nose2` to make sure that all tests are passing
* Run `flask run`
* Visit [localhost:5000](http://localhost:5000) in a browser

As an alternative, you can also run `./boot.sh` to spin up the server. 

### Login Credentials
```
username = 'user'
password = 'test'
```