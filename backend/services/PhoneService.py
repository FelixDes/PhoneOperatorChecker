from backend.config.PostgresConnectionPool import PostgresConnectionPool
from backend.exceptions.ServiceException import ServiceException


class PhoneService:

    def __init__(self, pg_pool: PostgresConnectionPool) -> None:
        self._pg_pool = pg_pool

    def get_provider(self, phone_number) -> str:
        try:
            conn = self._pg_pool.get_connection()
            cur = conn.cursor()

            cur.execute("select get_number_operator(" + phone_number + ");")
            rs = cur.fetchone()

            cur.close()
            self._pg_pool.put_connection(conn)
            return rs[0]
        except TypeError:
            raise ServiceException("Something went wrong during getting the operator name for " + phone_number)
