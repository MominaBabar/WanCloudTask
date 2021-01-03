FROM alpine:latest

RUN apk add --no-cache python3-dev
RUN apk add cmd:pip3
RUN pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt
RUN pip3 install mysqlclient-1.4.6-cp39-cp39-win32.whl
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["server.py", "runserver"]
