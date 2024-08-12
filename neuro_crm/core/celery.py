import logging
import os

from celery import Celery, Task
from kombu import Exchange, Queue

logger = logging.getLogger(__name__)

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neuro_crm.settings.local")


class BaseTask(Task):
    def __call__(self, *args, **kwargs):
        logger.info(f"Run task {self.name} args: {args!r}, kwargs: {kwargs!r}")
        return super(BaseTask, self).__call__(*args, **kwargs)

    def apply_async(
        self,
        args=None,
        kwargs=None,
        task_id=None,
        producer=None,
        link=None,
        link_error=None,
        shadow=None,
        **options,
    ):
        logger.info(
            f"Send task {self.name}, " f"args: {args!r}, kwargs: {kwargs!r}"
        )

        return super(BaseTask, self).apply_async(
            args=args,
            kwargs=kwargs,
            task_id=task_id,
            producer=producer,
            link=link,
            link_error=link_error,
            shadow=shadow,
            **options,
        )

    def run(self, *args, **kwargs) -> dict:
        """The body of the task executed by workers."""
        raise NotImplementedError("Tasks must define the run method.")


app = Celery("neuro_crm", task_cls=BaseTask)

app.config_from_object("django.conf:settings", namespace="CELERY")

NEURO_QUEUE = "neuro_queue"
NEURO_EXCHANGE = "neuro_exchange"
NEURO_KEY = "neuro_key"

app.conf.task_queues = (
    Queue(NEURO_QUEUE, Exchange(NEURO_EXCHANGE), routing_key=NEURO_KEY),
)

app.conf.task_default_queue = NEURO_QUEUE
app.conf.task_default_exchange = NEURO_EXCHANGE
app.conf.task_default_routing_key = NEURO_KEY

app.conf.task_routes = {
    "*": {"queue": NEURO_QUEUE, "routing_key": NEURO_KEY},
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
