import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.fixture
def superuser():
    return User.objects.create_superuser(
        email="email@email.email", password="111"
    )


@pytest.mark.django_db
class TestUsers:
    def test_user_admin(self, superuser, client):
        assert str(superuser)

        client.force_login(superuser)

        url = reverse(
            "admin:%s_%s_change" % ("users", "user"), args=(superuser.id,)
        )
        res = client.get(url)
        assert res.status_code == 200

        url = reverse("admin:%s_%s_changelist" % ("users", "user"))
        res = client.get(url)
        assert res.status_code == 200
