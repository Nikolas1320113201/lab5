FROM alpine:3.7
RUN apk add --update python3 py-pip
COPY . /laba3
WORKDIR /laba3
ENTRYPOINT ["python3"]
CMD ["test.py"]