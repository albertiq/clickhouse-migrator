import os
from dataclasses import dataclass, field


@dataclass
class ClickhouseClientSettings:
    host: str = field(default=os.getenv('DB_CLICKHOUSE_HOST', 'localhost'))
    port: int = field(default=os.getenv('DB_CLICKHOUSE_PORT', 9000))
    user: str = field(default=os.getenv('DB_CLICKHOUSE_USER', 'default'))
    password: str = field(default=os.getenv('DB_CLICKHOUSE_PASS', ''))
    database: str = field(default=os.getenv('DB_CLICKHOUSE_NAME', 'dwh'))
    migrations_home: str = field(default=os.getenv('DB_CLICKHOUSE_SQL_PATH', ''))
    secure: bool = field(default=os.getenv('DB_CLICKHOUSE_SECURE', False))
    verify: bool = field(default=os.getenv('DB_CLICKHOUSE_VERIFY', False))
    ca_certs: str = field(default=os.getenv('DB_CLICKHOUSE_CA_CERTS', ''))


clickhouse_client_config = ClickhouseClientSettings()
