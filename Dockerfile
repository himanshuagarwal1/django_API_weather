FROM python:3



ENV PYTHONUNBUFFERED=1

WORKDIR /django-tech-test

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /django-tech-test/




