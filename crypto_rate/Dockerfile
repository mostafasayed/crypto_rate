FROM python:3.9.5

# set work directory
WORKDIR /usr/src/app


RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


COPY . /usr/src/app/
COPY ./crypto_rate/.env /usr/src/app/crypto_rate

