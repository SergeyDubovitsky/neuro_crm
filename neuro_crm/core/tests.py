from unittest.mock import patch

from neuro_crm.core.tasks import debug_task


@patch("neuro_crm.core.celery.Task.apply_async")
def test_debug_task(apply_mock):
    debug_task.apply_async()
    assert apply_mock.call_count == 1

    assert debug_task.run() is True
