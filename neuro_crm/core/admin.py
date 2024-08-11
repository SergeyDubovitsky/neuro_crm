from django.urls import reverse

# url = reverse(
#     "admin:%s_%s_change" % ("users", "user"), args=(superuser.id,)
# )
# res = client.get(url)
# assert res.status_code == 200
#
# url = reverse("admin:%s_%s_changelist" % ("users", "user"))


def get_admin_change_url(app: str, model: str, obj_id: int) -> str:
    return reverse("admin:%s_%s_change" % (app, model), args=(obj_id,))


def get_admin_changelist_url(app: str, model: str) -> str:
    return reverse("admin:%s_%s_changelist" % (app, model))
