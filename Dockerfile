# [Optional] Uncomment this section to install additional OS packages.
FROM python:3.10-buster

WORKDIR /app
COPY . .

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends curl

# Poetry package manager
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["poetry", "run", "dev"]
