import pytest
from specialists.factories import SpecialistFactory, SpecialityFactory

from neuro_crm.core.admin import get_admin_change_url, get_admin_changelist_url


@pytest.mark.django_db
class TestSpecialists:
    def test_speciality_admin(self, client, admin_user):
        client.force_login(admin_user)

        speciality = SpecialityFactory()
        speciality.save()

        url = get_admin_change_url("specialists", "speciality", speciality.id)
        res = client.get(url)
        assert res.status_code == 200

        url = get_admin_changelist_url("specialists", "speciality")
        res = client.get(url)
        assert res.status_code == 200

    def test_specialist_admin(self, client, admin_user):
        client.force_login(admin_user)

        specialist = SpecialistFactory.create()

        url = get_admin_change_url("specialists", "specialist", specialist.id)
        res = client.get(url)
        assert res.status_code == 200

        url = get_admin_changelist_url("specialists", "specialist")
        res = client.get(url)
        assert res.status_code == 200
