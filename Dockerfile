FROM python:3.7.9-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/Makku_BackEnd_Users
COPY ./requirements.txt .

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install psycopg2==2.9.5
RUN pip install psycopg2-binary==2.8.6
RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 5432

COPY . .

ENTRYPOINT ["/usr/src/Makku_BackEnd_Users/entrypoint.sh"]