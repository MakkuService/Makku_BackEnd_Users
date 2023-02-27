FROM python:3.7.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/Makku_Backend

WORKDIR /usr/src/Makku_Backend
COPY . /usr/src/Makku_Backend
#WORKDIR /usr/src/Makku_Backend

#ADD . /Makku_Backend/

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install psycopg2==2.9.5
RUN pip install psycopg2-binary==2.8.6
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
