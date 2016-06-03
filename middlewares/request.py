from configs import settings
from middlewares.exceptions import abort

__all__ = ['middleware_request', 'middleware_request_validate']


async def middleware_request_validate(app, handler):
    async def middleware_handler(request):
        token_partner = request.headers.get('X-Auth-Token', '')
        if token_partner not in settings.TOKENS_PARTNERS:
            abort(403, 'Not token partners')

        request['partner_methods'] = settings.TOKENS_PARTNERS.get(token_partner)

        return await handler(request)

    return middleware_handler


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
