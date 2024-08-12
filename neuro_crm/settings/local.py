from neuro_crm.settings.base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ["django_extensions"]

STORAGES = {
    "default": {
        "BACKEND": "neuro_crm.core.storages.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "neuro_crm.core.storages.StaticStorage",
    },
}

AWS_ACCESS_KEY_ID = MINIO_ROOT_USER
AWS_SECRET_ACCESS_KEY = MINIO_ROOT_PASSWORD
AWS_STORAGE_BUCKET_NAME = MINIO_BUCKET_NAME
AWS_S3_ENDPOINT_URL = MINIO_ENDPOINT
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = True
AWS_S3_FILE_OVERWRITE = True
