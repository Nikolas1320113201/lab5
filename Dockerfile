FROM alpine:3.7
RUN apk add --update python3 py-pip
COPY . /lab_5
WORKDIR /lab_5
ENTRYPOINT ["python3"]
CMD ["test.py"]
