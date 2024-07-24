from config import clickhouse_client_config as cfg
from migrate import migrate

if __name__ == "__main__":
    while True:
        try:
            migrate(
                cfg.database,
                cfg.migrations_home,
                cfg.host,
                cfg.user,
                cfg.password,
                cfg.port,
                cfg.secure,
                cfg.verify,
                cfg.ca_certs,
            )
        except Exception as e:
            print(f"Error during migration: {str(e)}")
