from clients.factories import ClientFactory

from neuro_crm.core.admin import get_admin_change_url, get_admin_changelist_url


class TestClients:
    def test_clients(self, client, admin_user):
        client.force_login(admin_user)

        client_obj = ClientFactory()

        url = get_admin_change_url("clients", "client", client_obj.id)
        resp = client.get(url)
        assert resp.status_code == 200

        url = get_admin_changelist_url("clients", "client")
        resp = client.get(url)
        assert resp.status_code == 200
