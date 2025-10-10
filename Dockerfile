FROM python:3.13.2

WORKDIR /app

COPY . /app

RUN pip install flask flask-mysqldb

EXPOSE 3000

CMD [ "python", "app.py" ]