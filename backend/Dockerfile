FROM python:3.10

WORKDIR /backend
COPY requirements.txt /backend
RUN pip install --upgrade pip && python -m pip install -r requirements.txt

EXPOSE 5000
ENV PROD 1
COPY . /backend
