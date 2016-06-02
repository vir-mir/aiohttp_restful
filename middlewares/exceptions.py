import json

from aiohttp import web
from aiohttp.web_exceptions import HTTPException

__all__ = ['middleware_exception']


async def middleware_exception(app, handler):
    async def middleware_handler(request):
        try:
            return await handler(request)
        except HTTPException as e:
            if not type(e) == HTTPExceptionJson:
                return HTTPExceptionJson(status_code=e.status, text=e.reason)
            return e

    return middleware_handler


def abort(status, text, *, help_text=''):
    if type(text) is not [dict, list]:
        text = {
            'message': text
        }
    if help_text:
        text['help'] = help_text

    raise HTTPExceptionJson(status_code=status, text=text)


class HTTPExceptionJson(HTTPException):
    status_code = None
    empty_body = False

    def __init__(self, *, status_code=None, headers=None, reason=None,
                 body=None, text=None, content_type=None):
        self.status_code = status_code
        if type(text) is str:
            text = {'message': text}

        text = json.dumps(text)

        web.Response.__init__(self, status=self.status_code,
                              headers=headers, reason=reason,
                              body=body, text=text, content_type=content_type)
        Exception.__init__(self, self.reason)
        if self.body is None and not self.empty_body:
            self.text = self.text
