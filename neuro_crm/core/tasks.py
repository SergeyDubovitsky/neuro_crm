import logging
import time

from neuro_crm.core import celery_app
from neuro_crm.core.celery import BaseTask

logger = logging.getLogger(__name__)


class DebugTask(BaseTask):
    def run(self, *args, **kwargs):
        time.sleep(2)
        logger.info(f"Request: {self.request!r}")
        return True


debug_task = celery_app.register_task(DebugTask())
