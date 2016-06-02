import aiohttp_autoreload
from aiohttp import web

import middlewares
from configs import settings, urls

if __name__ == '__main__':
    if settings.DEBUG:
        aiohttp_autoreload.start()

    middleware = [getattr(middlewares, x) for x in middlewares.__all__]

    app = web.Application(debug=settings.DEBUG, middlewares=middleware)

    [app.router.add_route(*x) for x in urls.urls]

    web.run_app(app, port=settings.PORT)
