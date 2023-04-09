FROM python:3.9-slim-buster

WORKDIR /app

ADD requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD /src /app
ADD .env /app/

CMD ["python3.9", "app.py"]