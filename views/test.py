from aiohttp import web

from middlewares.exceptions import abort
from utils import fields
from utils import view

ddd = "asdasdasdasdasdasd"


class Test(view.View):
    class Meta:
        text = fields.FieldCompare(larger=1, less=2)
        text4 = fields.FieldInteger()

    async def get(self):
        """{"a": 1212321, "b": {"sadas": true}}"""

        abort(401, 'asfasfasf')
        return web.json_response({})

    async def post(self):
        return web.json_response({}, status=201)
