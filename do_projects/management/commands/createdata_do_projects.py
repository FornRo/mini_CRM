import random

from django.core.management.base import BaseCommand

from faker import Faker

from random import randint

from do_projects.models import DoProject
from customer_info.models import Company


class Command(BaseCommand):
    help = "Comand information"

    def __init__(self):
        super().__init__()
        self.fake = Faker(['en'])

    def handle(self, *args, **options):
        self.generate_do_project()

    def generate_do_project(self):
        count_company = Company.objects.count()
        DoProject.objects.bulk_create(
            [
                DoProject(
                    name_project=self.fake.catch_phrase(),
                    description=self.fake.text(max_nb_chars=200),
                    start_date=self.fake.past_date(),
                    end_date=self.fake.future_date(end_date=62),
                    cost=round(random.random() * 10000, 2),
                    company=Company.objects.get(id=randint(1, count_company)),
                )
                for _ in range(200 + 1)
            ]
        )
        check_val = DoProject.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'Generate of DoProject {check_val}'))
