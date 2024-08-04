import os  # noqa
from neuro_crm.settings.base import *  # noqa

DEBUG = False
DOMAIN = os.getenv("DOMAIN", "localhost")
ALLOWED_HOSTS = [DOMAIN]
