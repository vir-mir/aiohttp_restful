from configs import settings
from middlewares.exceptions import abort

__all__ = ['middleware_request']


async def middleware_request(app, handler):
    async def middleware_handler(request):
        version = list(filter(lambda x: x.lower().startswith('application/request'), request.headers.getall('Accept')))

        if any(version):
            version = version[0]
        else:
            version = settings.VERSION

        content_type = request.headers.get('Content-Type', None)
        version, type_ = version.split('.').pop().split('+')

        if content_type == 'application/json' or type_ == 'json':
            type_ = 'json'
        else:
            abort(400, 'Not Method')

        request['version'] = version
        request['type'] = type_

        return await handler(request)

    return middleware_handler
