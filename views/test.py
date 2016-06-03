from aiohttp import web

from utils import fields
from utils import view

ddd = "asdasdasdasdasdasd"


class Test(view.View):
    class Meta:
        text = fields.FieldCompare(larger=1, less=56, required=False)
        text4 = fields.FieldInteger(verbose_name='id_name')

    async def get(self):
        """{"a": 1212321, "b": {"sadas": true}}"""

        return web.json_response({})
