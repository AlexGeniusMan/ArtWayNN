FROM python:3.7.9-slim

RUN pip install --upgrade pip

WORKDIR /src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN pytest

CMD python run.py