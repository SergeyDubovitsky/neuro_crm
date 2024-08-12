import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: "user{}@example.com".format(n))
    is_active = True
    is_staff = False
    is_superuser = False
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    middle_name = factory.Faker("last_name")
    password = factory.Faker("password")
    phone = factory.Sequence(lambda n: "+7963000{}".format(n))
