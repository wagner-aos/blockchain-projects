.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help
SHELL := /bin/bash

SERVER_HORT=127.0.0.0
SERVER_PORT=8000

DATABASE_NAME=postgres
DATABASE_USERNAME=postgres
PGPASSWORD=h234siufyds43
DATABASE_HOST=localhost
DATABASE_PORT=5432

# PYTHON
install-python-linux:
	sudo apt-get install python3.11
	python --version
	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
	sudo update-alternatives --config python3
	sudo apt-get install python3.11-venv

# Database
start-docker-database:
	docker run --name postgresql-container -p ${DATABASE_PORT}:${DATABASE_PORT} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -d ${DATABASE_NAME}

load-database:
	PGPASSWORD=${PGPASSWORD} psql -h ${DATABASE_HOST} -p ${DATABASE_PORT} -U ${DATABASE_USERNAME} \
	-d ${DATABASE_NAME} -f scripts/init-db.sql

connect-db:
	PGPASSWORD=${PGPASSWORD} psql -h ${DATABASE_HOST} -p ${DATABASE_PORT} -U ${DATABASE_USERNAME} -d ${DATABASE_NAME}

# Project Dependencies
install-depenpencies:
	pip3 install --editable .

clear-pip-depenpencies:
	$(eval user_name := $(shell whoami))
	rm -rf /home/${user_name}/.local/lib/python3.11/site-packages
	rm -rf ./venv
	deactivate

# Start API
virtual-env:
	python3.11 -m venv venv && source venv/bin/activate

virtual-env-deactivate:
	deactivate

start:
	uvicorn app.main:app --host ${SERVER_HORT} --port ${SERVER_PORT}

# Docs
swagger:
	google-chrome http://${SERVER_HORT}:${SERVER_PORT}/docs

# API Tests
api-get-token:
	curl -X 'POST' 'http://${SERVER_HORT}:${SERVER_PORT}/token' \
	-d 'username=test_user@myapi.com&password=password'