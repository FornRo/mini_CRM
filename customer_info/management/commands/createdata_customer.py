from django.core.management.base import BaseCommand

from faker import Faker
from random import randint

from customer_info.models import *


class Command(BaseCommand):
    help = "This command created fake.data to customer_info.model.Company & PhoneNumber & Email"

    def __init__(self):
        super().__init__()
        self.fake = Faker(['en'])

    def handle(self, *args, **options) -> None:
        self.generate_phone_number()
        self.generate_email()
        self.generate_company()

    def generate_phone_number(self) -> None:
        if PhoneNumber.objects.count() == 0:
            PhoneNumber.objects.bulk_create(
                [
                    PhoneNumber(phone_number=self.fake.phone_number())
                    for _ in range(100 + 1)
                ]
            )
            check_val = PhoneNumber.objects.count()
            self.stdout.write(self.style.SUCCESS(f'Generate of PhoneNumber {check_val}'))
        else:
            self.stdout.write(self.style.SUCCESS('DB has PhoneNumber'))

    def generate_email(self) -> None:
        if Email.objects.count() == 0:
            Email.objects.bulk_create(
                [
                    Email(e_mail=self.fake.company_email())
                    for _ in range(100 + 1)
                ]
            )
            check_val = Email.objects.count()
            self.stdout.write(self.style.SUCCESS(f'Generate of Email {check_val}'))
        else:
            self.stdout.write(self.style.SUCCESS('DB has Email'))

    def generate_company(self) -> None:
        count_phone_number = PhoneNumber.objects.count()
        count_email = Email.objects.count()
        if Company.objects.count() == 0:
            for val in range(35):
                company = Company(
                    name_company=self.fake.company(),
                    name=self.fake.name(),
                    description=self.fake.text(max_nb_chars=120),
                    created_date=self.fake.past_date(),  # -(1 < n <= 30) day
                    change_date=None,
                    address=self.fake.address(),
                )
                company.save()

                # chose random phone_number "amount 1 <= n <= 3" from models.PhoneNumber
                for object_phone_number in [PhoneNumber.objects.get(id=randint(1, count_phone_number))
                                            for _ in range(randint(1, 3))]:
                    company.phone_number.add(object_phone_number)

                # chose random email "amount 1 <= n <= 3" from models.Email
                for object_email in [Email.objects.get(id=randint(1, count_email))
                                     for _ in range(randint(1, 3))]:
                    company.e_mail.add(object_email)

            else:
                check_val = Company.objects.count()
                self.stdout.write(self.style.SUCCESS(f'Generate of Company {check_val}'))
        else:
            self.stdout.write(self.style.SUCCESS('DB has Company'))
