FROM python:3.10.8-alpine3.16
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD python main.py