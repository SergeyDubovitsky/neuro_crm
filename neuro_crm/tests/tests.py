import pytest
from django.urls import reverse


@pytest.mark.asyncio
async def test_healthcheck(async_client):
    resp = await async_client.get(reverse("api:healthcheck"))
    assert resp.status_code == 200
    assert resp.json()
