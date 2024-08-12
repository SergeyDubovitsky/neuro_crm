import factory
from courses.models import Course


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    payer = factory.SubFactory("users.factories.UserFactory")
    specialist = factory.SubFactory("specialists.factories.SpecialistFactory")
