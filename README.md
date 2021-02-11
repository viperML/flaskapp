# Flask Web application

- Personal project to build a personal web page.
- Using the flask python framework.
- Deployed using Docker containers and systemd with Nginx and PostgreSQL.
- TLS encryption
- Currently hosted by Amazon Web Services at [viper.cafe](https://viper.cafe)

## Requirements:
- Ubuntu 18.04
- Docker

## To-Do:
- [ ] Add content to the templates
- [ ] Implement CI/CD
- [ ] Keep python dependencies updated

## Deployment (for future reference)
```
# systemctl enable /home/ubuntu/flaskapp/portfolio.service
# systemctl restart portfolio.service
```