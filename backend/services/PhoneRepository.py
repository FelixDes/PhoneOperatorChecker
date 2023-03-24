from backend.config.PostgresConnectionPool import PostgresConnectionPool


class PhoneRepository:

    def __init__(self, pg_pool: PostgresConnectionPool) -> None:
        self.pg_pool = pg_pool

    def get_provider(self, phone_number) -> str:
        return phone_number
