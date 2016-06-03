import aiopg
import psycopg2.extras
from psycopg2 import ProgrammingError

from configs import settings

__all__ = ['DB']


class DB:
    def __init__(self):
        self.__dsn = 'dbname={database} user={user} password={password} host={host}'.format(**settings.DATE_BASE)
        self.__pool = None
        self.__conn = None

    async def __aenter__(self):
        self.__pool = await aiopg.create_pool(self.__dsn)
        self.__conn = await self.__pool.acquire()
        return self

    async def select(self, query: str, params=None):
        async with self.__conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cur:
            await cur.execute(query, params)
            rows = await cur.fetchall()
        return rows

    async def get(self, query: str, params=None):
        async with self.__conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as cur:
            await cur.execute(query, params)
            row = await cur.fetchone()
        return row

    async def insert(self, query: str, params=None):
        async with self.__conn.cursor() as cur:
            await cur.execute(query, params)
            try:
                id_ = await cur.fetchone()
            except ProgrammingError:
                id_ = [None]
        return id_[0]

    async def update(self, query: str, params=None):
        async with self.__conn.cursor() as cur:
            await cur.execute(query, params)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.__conn.close()
        self.__pool.close()
