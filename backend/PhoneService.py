from typing import Any

import PostgresConnectionPool
from ServiceException import ServiceException


class PhoneService:

    def __init__(self, pg_pool: PostgresConnectionPool) -> None:
        self._pg_pool = pg_pool

    def get_data(self, phone_number) -> list[Any]:
        try:
            conn = self._pg_pool.get_connection()
            cur = conn.cursor()

            cur.execute("select get_number_provider(" + phone_number + ");")
            r1 = cur.fetchone()

            cur.execute("select get_number_region(" + phone_number + ");")
            r2 = cur.fetchone()

            cur.close()
            self._pg_pool.put_connection(conn)
            return [r1[0], r2[0]]
        except TypeError:
            raise ServiceException("Something went wrong during getting the operator name for " + phone_number)
