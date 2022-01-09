from django.core.management.base import BaseCommand

import faker.providers
import faker.proxy
from faker import Faker
from random import randint

from customer_info import models


class Provider(faker.providers.BaseProvider):
    pass


# ------------------------------------------------------------
class Command(BaseCommand):
    help = "Comand information"

    def __init__(self):
        super().__init__()
        self.fake = Faker(['en'])

    def handle(self, *args, **options):
        self.fake.add_provider(Provider)

        self.generate_phone_number()
        self.generate_email()
        self.generate_company()

    def generate_phone_number(self):
        models.PhoneNumber.objects.bulk_create(
            [
                models.PhoneNumber(
                    phone_number=self.fake.phone_number(),
                )
                for _ in range(100 + 1)
            ]
        )
        check_val = models.PhoneNumber.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'Generate of PhoneNumber {check_val}'))

    def generate_email(self):
        models.Email.objects.bulk_create(
            [
                models.Email(
                    e_mail=self.fake.company_email(),
                )
                for _ in range(100 + 1)
            ]
        )
        check_val = models.Email.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'Generate of Email {check_val}'))

    def generate_company(self):
        from . import _data
        count_phone_number = models.PhoneNumber.objects.count()
        count_email = models.Email.objects.count()
        if models.Company.objects.count() == 0:
            for val in _data.company_name:
                company = models.Company(
                    name_company=val,
                    name=self.fake.name(),
                    description=self.fake.text(max_nb_chars=120),
                    created_date=self.fake.past_date(),  # -(1 < n <= 30) day
                    # change_date=random.choice([None, self.fake.past_date('-28d')]),  # -(1 < n <= 28) day
                    change_date=None,
                    address=self.fake.address(),
                    # phone_number=self.fake.phone_number(),
                    # e_mail=self.fake.company_email(),
                )
                company.save()

                # chose random phone_number "some 1 <= n <= 3" from models.PhoneNumber
                for object_phone_number in [models.PhoneNumber.objects.get(id=randint(1, count_phone_number))
                                            for _ in range(randint(1, 3))]:
                    company.phone_number.add(object_phone_number)

                # chose random email "some 1 <= n <= 3" from models.Email
                for object_email in [models.Email.objects.get(id=randint(1, count_email))
                                     for _ in range(randint(1, 3))]:
                    company.e_mail.add(object_email)

            else:
                check_val = models.Company.objects.all().count()
                self.stdout.write(self.style.SUCCESS(f'Generate of Company {check_val}'))
