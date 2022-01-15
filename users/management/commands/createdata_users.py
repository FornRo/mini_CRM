from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand
from faker import Faker

from users.models import Profile


class Command(BaseCommand):
    help = "This command created fake.data to users.model.User & Group & auto Profile add "

    def __init__(self):
        super().__init__()
        self.fake = Faker(['en'])

    def handle(self, *args, **options):
        self.generate_groups()
        self.generate_users()

    def generate_users(self) -> None:
        if User.objects.count() <= 1:
            for i in range(15):
                groups = Group.objects.get(name=
                                           ('managers' if i >= 10 else 'users'))
                user = User(
                    username=self.fake.name(),
                    password=self.fake.password(length=12),
                    email=self.fake.email(),
                    first_name=self.fake.first_name(),
                    last_name=self.fake.last_name(),
                )
                user.save()
                user.groups.add(groups)
            check_val = User.objects.count()
            self.stdout.write(self.style.SUCCESS(f'Generate of Users {check_val}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'You have user`s more 1 '))

    def generate_groups(self) -> None:
        if Group.objects.count() == 0:
            group_reg_user = Group.objects.get_or_create(name='users')
            group_manager = Group.objects.get_or_create(name='managers')

            # group_reg_user.permissions.set([
            #     catalog.add_author
            # ])

            self.stdout.write(self.style.SUCCESS('Created Groups: "users" & "managers"'))
        else:
            self.stdout.write(self.style.SUCCESS('DB has groups'))

