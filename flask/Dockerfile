FROM python:3.8.5-buster

# Python dependencies
COPY requirements.txt /
RUN pip install -r requirements.txt

# App files
WORKDIR /portfolio
# Run app
CMD ["uwsgi", "app.ini"]