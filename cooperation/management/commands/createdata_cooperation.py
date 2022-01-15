from django.core.management.base import BaseCommand

from faker import Faker
from random import randint, choice

from do_projects.models import DoProject
from cooperation.models import Cooperation, CHANNEL, RATING


class Command(BaseCommand):
    help = "This command created fake.data to cooperation.model.Cooperation"

    def __init__(self):
        super().__init__()
        self.fake = Faker(['en'])

    def handle(self, *args, **options) -> None:
        self.generate_cooperation()

    def generate_cooperation(self) -> None:
        count_do_project = DoProject.objects.count()
        if Cooperation.objects.count() == 0:
            Cooperation.objects.bulk_create(
                [
                    Cooperation(
                        project=DoProject.objects.get(id=randint(1, count_do_project)),
                        name_manager=self.fake.name(),
                        description=self.fake.text(max_nb_chars=200),
                        channel_of_usage=choice([val[0] for val in CHANNEL]),
                        rating=choice([val[0] for val in RATING]),
                    )
                    for _ in range(400)
                ]
            )
            check_val = Cooperation.objects.count()
            self.stdout.write(self.style.SUCCESS(f'Generate of Cooperation {check_val}'))
        else:
            self.stdout.write(self.style.SUCCESS('DB has Cooperation'))
