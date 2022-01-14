from django.core.management.base import BaseCommand

from faker import Faker
from random import randint

from users.models import Profile, User

class Command(BaseCommand):
    help = "Comand information"

    def __init__(self):
        super().__init__()
        self.fake = Faker(['en'])

    def handle(self, *args, **options):
        self.generate_users()
        self.generate_profile()

    def generate_users(self):
        user_obj_list = []
        for _ in range(25):
            password = self.fake.password(length=12)
            a = User(username=self.fake.name(),)
            a.set_password(password)
            user_obj_list.append(a)

        User.objects.bulk_create(
            user_obj_list
        )
        check_val = User.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'Generate of Users {check_val}'))

    def generate_profile(self):
        count_user = User.objects.count()
        Profile.objects.bulk_create(
            [
                Profile(
                    company=User.objects.get(id=randint(1, count_user)),
                )
                for _ in range(count_user)
            ]
        )
        check_val = Profile.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'Generate of Profile {check_val}'))
