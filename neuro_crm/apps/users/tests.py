import pytest
from django.contrib.auth import get_user_model

from neuro_crm.core.admin import get_admin_change_url, get_admin_changelist_url

User = get_user_model()


@pytest.mark.django_db
class TestUsers:
    def test_user_admin(self, admin_user, client):
        assert str(admin_user)

        client.force_login(admin_user)

        url = get_admin_change_url("users", "user", admin_user.id)
        res = client.get(url)
        assert res.status_code == 200

        url = get_admin_changelist_url("users", "user")
        res = client.get(url)
        assert res.status_code == 200
