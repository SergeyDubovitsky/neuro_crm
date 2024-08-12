import factory
from clients.models import Client


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    full_name = factory.Faker("name")
    birth_date = factory.Faker("date_of_birth")
    user = factory.SubFactory("users.factories.UserFactory")
