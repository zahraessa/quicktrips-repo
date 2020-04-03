FROM python:3.6-jessie

RUN apt update
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN pip install python-dotenv
ADD . /app
ENV PORT 5000


CMD ["gunicorn", "app:app", "--config=config.py"]
#CMD ["/bin/bash", "entrypoint.sh"]

#CMD ["python", "app.py"]