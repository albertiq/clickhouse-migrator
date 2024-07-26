from config import clickhouse_client_config as cfg
from migrate import migrate

if __name__ == "__main__":
    while True:
        try:
            migrate(
                db_name=cfg.database,
                migrations_home=cfg.migrations_home,
                db_host=cfg.host,
                db_user=cfg.user,
                db_password=cfg.password,
                db_port=cfg.port,
                secure=cfg.secure,
                verify=cfg.verify,
                ca_certs=cfg.ca_certs,
                certfile=cfg.certfile,
                keyfile=cfg.keyfile,
            )
            break
        except Exception as e:
            print(f"Error during migration: {str(e)}")
