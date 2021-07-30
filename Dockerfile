# Dockerfile
FROM python:3.9
WORKDIR /fastapi_authors
COPY . /fastapi_authors
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]