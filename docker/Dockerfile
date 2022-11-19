FROM python:3.8-slim

# copy docker-entrypoint and requirements to initialize multi-stage build
COPY ./docker/docker-entrypoint.sh ./requirements.txt /app/

# implement multi-stage build to leverage build cache (does not re-install packages when code changes)
RUN pip install -r /app/requirements.txt

# copy source code
COPY ./src /app/src

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# expose docker container port 80 according to weeve spec
EXPOSE 80