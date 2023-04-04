import os

from dependency_injector import providers, containers
from dependency_injector.containers import DeclarativeContainer

from PhoneService import PhoneService
from PostgresConnectionPool import PostgresConnectionPool


class MainContainer(DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["PhoneControllers"])

    config = providers.Configuration()

    isProd = os.getenv('PROD', False)
    print("Production: " + str(isProd))
    if isProd:
        config.from_yaml("db_config_prod.yaml")
    else:
        config.from_yaml("db_config.yaml")

    pg_pool = providers.Singleton(PostgresConnectionPool, pg_config=config.postgres)
    phone_repository = providers.Factory(PhoneService, pg_pool=pg_pool)
