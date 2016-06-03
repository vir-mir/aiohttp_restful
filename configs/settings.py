DEBUG = False

PORT = 8005

DATE_BASE = {
    'user': 'vir-mir',
    'password': '',
    'host': 'localhost',
    'database': 'new_stromyc',
}

TOKENS_PARTNERS = {}

VERSION = 'application/request.v1+json'

try:
    from configs.local_settings import *
except ImportError:
    pass
