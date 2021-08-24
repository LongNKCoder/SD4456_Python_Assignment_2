FROM python:3.9.6-buster
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN cp ./backup/backupdb.sqlite3 ./assignment/db.sqlite3
