import aiopg

from configs.settings import DATE_BASE

__all__ = ['connect_db']


async def connect_db(app, handler):
    async def middleware(request):
        if getattr(handler, '_is_coroutine', False):
            return await handler(request)

        dsn = 'dbname=%s user=%s password=%s host=%s' % (
            DATE_BASE['database'], DATE_BASE['user'], DATE_BASE['password'], DATE_BASE['host']
        )
        pool = await aiopg.create_pool(dsn)
        async with pool.acquire() as conn:
            request['conn'] = conn
            response = await handler(request)
            return response

    return middleware
