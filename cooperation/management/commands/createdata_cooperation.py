from django.core.management.base import BaseCommand

from faker import Faker
from random import randint, choice

from do_projects.models import DoProject
from cooperation import models as cooper_models


class Command(BaseCommand):
    help = "Comand information"

    def __init__(self):
        super().__init__()
        self.fake = Faker(['en'])

    def handle(self, *args, **options):
        self.generate_cooperation()

    def generate_cooperation(self):
        count_do_project = DoProject.objects.count()
        if cooper_models.Cooperation.objects.count() == 0:
            cooper_models.Cooperation.objects.bulk_create(
                [
                    cooper_models.Cooperation(
                        project=DoProject.objects.get(id=randint(1, count_do_project)),
                        name_manager=self.fake.name(),
                        description=self.fake.text(max_nb_chars=200),
                        channel_of_usage=choice([val[0] for val in cooper_models.CHANNEL]),
                        rating=choice([val[0] for val in cooper_models.RATING]),
                    )
                    for _ in range(325)
                ]
            )
            check_val = cooper_models.Cooperation.objects.all().count()
            self.stdout.write(self.style.SUCCESS(f'Generate of Cooperation {check_val}'))
