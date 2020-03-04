FROM python:3.6-alpine

RUN apk update \
    && apk add --virtual build-dependencies \
        build-base \
        gcc \
        wget \
        git \
    && apk add \
        bash

COPY . /app
WORKDIR /app

RUN \
 apk add --no-cache bash && \
 apk add libffi-dev && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install -r requirements.txt


EXPOSE 5000

ENV FLASK_APP=app.py

ENTRYPOINT [ "flask" ]

CMD [ "run" ]
