FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends \
    git \
    curl \
    wget

RUN useradd -ms /bin/bash python

RUN pip install pdm

USER python

WORKDIR /home/python/app

ENV MY_PYTHON_PACKAGES=/home/python/__pypackages__/3.10
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENTRYPOINT PATH $PATH:${MY_PYTHON_PACKAGES}/bin

CMD [ "tail", "-f", "/dev/null" ]