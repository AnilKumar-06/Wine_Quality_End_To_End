from python:3.8-slim-buster

RUN app update -y && apt install awscli -y
WORKDIR/app

COPY ./app
Run pip install -r requirements.txt
CMD ["python", "app.py"]