import logging
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

            cur.execute("select get_original_number_provider(" + phone_number + ");")
            original_provider = cur.fetchone()

            cur.execute("select get_current_number_provider(" + phone_number + ");")
            current_provider = cur.fetchone()

            cur.execute("select get_number_region(" + phone_number + ");")
            region = cur.fetchone()

            cur.close()
            return [original_provider[0], current_provider[0], region[0]]
        except TypeError:
            raise ServiceException("Something went wrong during getting the operator name for " + phone_number)
