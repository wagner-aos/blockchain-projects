.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help
SHELL := /bin/bash

PYTHON_VERSION=3.11

# API
SERVER_HORT=localhost
SERVER_PORT=8000
API_USER_NAME=test_user
API_USER_PASSWORD=password
API_USER_EMAIL=test_user@myapi.com
# Database
DATABASE_NAME=postgres
DATABASE_USERNAME=postgres
PGPASSWORD=h234siufyds43
DATABASE_HOST=localhost
DATABASE_PORT=5432

# PYTHON
install-python-linux:
	sudo apt-get install python${PYTHON_VERSION}
	python --version
	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 2
	sudo update-alternatives --config python3
	sudo apt-get install python${PYTHON_VERSION}-venv

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
	rm -rf /home/${user_name}/.local/lib/python${PYTHON_VERSION}/site-packages
	rm -rf ./venv
	deactivate

# Start API
virtual-env:
	python${PYTHON_VERSION} -m venv venv && source venv/bin/activate

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
#{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoidGVzdCB1c2VyIiwic3ViIjoidGVzdF91c2VyQG15YXBpLmNvbSIsImV4cGlyZXNfYXQiOiIyMDIzLTA4LTI3IDE2OjM5OjA5In0.bfaMjRJfjSLfb1g4UIJ2E0OQGRWOfrfagkMym5ngsfg","token_type":"bearer"}

api-get-access-token:
	$(eval ACCESS_TOKEN := $(shell curl -X 'POST' 'http://${SERVER_HORT}:${SERVER_PORT}/token' \
	-d 'username=${API_USER_EMAIL}&password=${API_USER_PASSWORD}' | jq .access_token | tr -d '"'))

api-get-movies: api-get-access-token
	@curl -X 'GET' 'http://${SERVER_HORT}:${SERVER_PORT}/movies/new?year=1990&rating=6' \
	-H 'Authorization: Bearer ${ACCESS_TOKEN}' | jq --color-output .

api-get-movie-byid: api-get-access-token # CALL: make api-get-movie-byid movieid=1
	@curl -X 'GET' 'http://${SERVER_HORT}:${SERVER_PORT}/movies/?movie_id=$(movieid)' \
	-H 'Authorization: Bearer ${ACCESS_TOKEN}' | jq --color-output .	
	@if [ -z "$(movieid)" ]; then echo "Example: make api-get-movie-byid movieid=1"; fi

#[{"movie_id":1,"title":"The Shawshank Redemption","released":1994,"rating":9.2},{"movie_id":3,"title":"The Dark Knight","released":2008,"rating":9.0}]%

#curl -X 'POST' 'http://127.0.0.0:8000/token' -d 'username=test_user@myapi.com&password=password' \
#| jq .access_token