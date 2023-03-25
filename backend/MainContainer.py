from dependency_injector import providers, containers
from dependency_injector.containers import DeclarativeContainer

from backend.config.PostgresConnectionPool import PostgresConnectionPool
from backend.services.PhoneService import PhoneService


class MainContainer(DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".controllers.PhoneControllers"])

    config = providers.Configuration()
    config.from_yaml("db_config.yaml")

    pg_pool = providers.Singleton(PostgresConnectionPool, pg_config=config.postgres)
    phone_repository = providers.Factory(PhoneService, pg_pool=pg_pool)
