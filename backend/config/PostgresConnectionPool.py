import psycopg2 as psycopg2
from psycopg2 import pool


class PostgresConnectionPool:
    _pg_pool = None

    def __init__(self, pg_config) -> None:
        self._pg_pool = psycopg2.pool.SimpleConnectionPool(1, 20, user=pg_config["user"],
                                                           password=pg_config["password"],
                                                           host=pg_config["host"],
                                                           port=pg_config["port"],
                                                           database=pg_config["db"])
        if self._pg_pool:
            print("Connection pool created successfully")

    def get_connection(self):
        return self._pg_pool.getconn()

    def put_connection(self, conn):
        return self._pg_pool.putconn(conn)
