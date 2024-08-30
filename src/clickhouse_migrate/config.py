import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ClickhouseClientSettings:
    host: str = field(default=os.getenv("DB_CLICKHOUSE_HOST", "localhost"))
    port: int = field(default=os.getenv("DB_CLICKHOUSE_PORT", 9000))
    user: str = field(default=os.getenv("DB_CLICKHOUSE_USER", "default"))
    password: str = field(default=os.getenv("DB_CLICKHOUSE_PASS", ""))
    database: str = field(default=os.getenv("DB_CLICKHOUSE_NAME", "dwh"))
    migrations_home: str = field(default=os.getenv("DB_CLICKHOUSE_SQL_PATH", Path("./sql/")))
    secure: Optional[bool] = field(default=os.getenv("DB_CLICKHOUSE_SECURE"))
    verify: Optional[bool] = field(default=os.getenv("DB_CLICKHOUSE_VERIFY"))
    ca_certs: Optional[str] = field(default=os.getenv("DB_CLICKHOUSE_CA_CERTS", Path("./certs/clickhouse-ca.crt")))
    certfile: Optional[str] = field(default=os.getenv("DB_CLICKHOUSE_CERT_FILE", Path("./certs/clickhouse.crt")))
    keyfile: Optional[str] = field(default=os.getenv("DB_CLICKHOUSE_KEY_FILE", Path("./certs/clickhouse.key")))


clickhouse_client_config = ClickhouseClientSettings()
