from courses.factories import CourseFactory

from neuro_crm.core.admin import get_admin_change_url, get_admin_changelist_url


class TestCourses:
    def test_courses(self, client, admin_user):
        client.force_login(admin_user)

        course = CourseFactory()

        url = get_admin_change_url("courses", "course", course.id)
        resp = client.get(url)
        assert resp.status_code == 200

        url = get_admin_changelist_url("courses", "course")
        resp = client.get(url)
        assert resp.status_code == 200
