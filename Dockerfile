FROM python:3.6-alpine3.7
WORKDIR /app

ADD stocktext /app
ADD app.py /app
COPY ./requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
