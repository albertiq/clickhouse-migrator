import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ClickhouseClientSettings:
    host: str = field(default=os.getenv("DB_CLICKHOUSE_HOST", "localhost"))
    port: int = field(default=os.getenv("DB_CLICKHOUSE_PORT"), init=False)
    secure_port: int = field(default=os.getenv("DB_CLICKHOUSE_SECURE_PORT"))
    user: str = field(default=os.getenv("DB_CLICKHOUSE_USER", "default"))
    password: str = field(default=os.getenv("DB_CLICKHOUSE_PASS", ""))
    database: str = field(default=os.getenv("DB_CLICKHOUSE_NAME", "dwh"))
    migrations_home: str = field(default=os.getenv("DB_CLICKHOUSE_SQL_PATH", Path("./sql/")))
    secure: Optional[bool] = field(init=False)
    verify: Optional[bool] = field(init=False)
    ca_certs: Optional[str] = field(default=os.getenv("DB_CLICKHOUSE_CA_CERTS_PATH"))
    certfile: Optional[str] = field(default=os.getenv("DB_CLICKHOUSE_CERT_FILE_PATH"))
    keyfile: Optional[str] = field(default=os.getenv("DB_CLICKHOUSE_KEY_FILE_PATH"))
    is_secure: Optional[bool] = field(init=False)

    def __post_init__(self):
        self.secure = self.get_bool_env("DB_CLICKHOUSE_SECURE", False)
        self.verify = self.get_bool_env("DB_CLICKHOUSE_VERIFY", False)
        self.is_secure = self.get_bool_env("IS_SECURE_CLICKHOUSE", False)

        self.port = self.secure_port if self.is_secure else self.port

    @staticmethod
    def get_bool_env(key: str, default: bool) -> bool:
        str_env = os.getenv(key)
        if str_env:
            return str_env.lower() in ("true", "1")
        return default


clickhouse_client_config = ClickhouseClientSettings()
