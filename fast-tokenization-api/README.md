# fast-tokenization-api

This repository provides an approach on how to effectively structure a FastAPI application 
with multiple services using 3-tier design pattern, integrate it with Postgres backend, 
and implement straightforward OAuth2 Password authentication flow using Bearer and 
JSON Web Tokens (JWT).

## How to execute

```bash
$ make start
```

## How to run

Configure the relevant DNS string to your Postgres backend database in `.env` file, 
or provide it from the environment variable `MYAPI_DATABASE_DNS`.

To run the application use following.

```bash
$ uvicorn app.main:app
```

or 

```bash
$ MYAPI_DATABASE_DNS=postgresql://... uvicorn app.main:app
```

## License

MIT License (see [LICENSE](LICENSE)).

### Links

https://www.infomoney.com.br/mercados/o-que-e-a-hyperledger-besu-a-tecnologia-escolhida-para-o-piloto-do-real-digital/