# Flask Web application

- Personal project to build a personal web page.
- Using the flask python framework.
- Deployed using Docker containers and systemd with Nginx and PostgreSQL.
- TLS encryption
- Currently hosted by Amazon Web Services at [viper.cafe](https://viper.cafe)

## Requirements:
- Ubuntu 18.04
- Docker Compose

## To-Do:
- [ ] Add content to the templates
- [ ] Implement CI/CD
- [ ] Keep python dependencies updated
- [ ] Include creation of PostgreSQL DB in Readme 

## Deployment (for future reference)
```
# systemctl enable /home/ubuntu/flaskapp/portfolio.service
# systemctl restart portfolio.service
```

## Testing Environment
```
$ export FLASK_ENV=development
$ cd flask
$ source ./env/bin/activate
$ python run.py
```

### Create local database for testing
```
$ export FLASK_ENV=development
$ cd flask
$ source ./env/bin/activate
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```