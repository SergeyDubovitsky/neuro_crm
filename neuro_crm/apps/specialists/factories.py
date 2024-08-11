import factory
from specialists.models import Specialist, Speciality
from users.factories import UserFactory


class SpecialityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Speciality

    name = factory.Faker("name")
    description = factory.Faker("text")


class SpecialistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Specialist

    full_name = factory.Faker("name")
    specialty = factory.SubFactory(SpecialityFactory)
    user = factory.SubFactory(UserFactory)
