from pydantic import (
    BaseModel,
    BaseSettings,
)


class DatabaseConfig(BaseModel):
    """Backend database configuration parameters.

    Attributes:
        DNS:
            DNS for target database.
    """

    DNS: str = "postgresql://postgres:h234siufyds43@localhost:5432/postgres"


class Config(BaseSettings):
    """API configuration parameters.

    Automatically read modifications to the configuration parameters
    from environment variables and ``.env`` file.

    Attributes:
        database:
            Database configuration settings.
            Instance of :class:`app.backend.config.DatabaseConfig`.
        token_key:
            Random secret key used to sign JWT tokens.
    """

    database: DatabaseConfig = DatabaseConfig()
    token_key: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "MYAPI_"
        env_nested_delimiter = "__"
        case_sensitive = False


config = Config()
