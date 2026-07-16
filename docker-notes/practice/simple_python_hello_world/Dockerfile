FROM alpine
RUN apk update && apk add --no-cache python3 py3-pip
WORKDIR /app
ADD hello.py hello.py
ENTRYPOINT python3 hello.py