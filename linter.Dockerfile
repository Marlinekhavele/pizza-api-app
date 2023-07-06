FROM 075050162388.dkr.ecr.eu-central-1.amazonaws.com/sennder/platform/python:buster-sam-3.11

LABEL maintainer="Mohamed Ali <mohamed.ali@sennder.com>"

ENV PRE_COMMIT_HOME=/.cache/pre-commit


RUN apt-get update && apt-get install -y git && apt-get clean && \
    pip install --no-cache-dir pre-commit==2.12.1 poetry==1.1.6

COPY .pre-commit-config.yaml .

# This will be cached as long as the hooks don't change:
RUN git init . && pre-commit install --install-hooks
