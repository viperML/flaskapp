FROM python:3.8.5-buster

# Dependecies before app files
COPY requirements.txt /
RUN pip install -r requirements.txt

# App files
WORKDIR /portfolio

# Run app
CMD ["uwsgi", "app.ini"]