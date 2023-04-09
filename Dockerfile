FROM python:3.9-slim-buster

WORKDIR /app

ADD /src /app
ADD requirements.txt /app/
ADD .env /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python3.9", "app.py"]