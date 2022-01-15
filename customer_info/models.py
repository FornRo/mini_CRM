from django.db import models

from ckeditor.fields import RichTextField


class Company(models.Model):
    name_company = models.CharField(max_length=200)  # Названия компании
    name = models.CharField(max_length=255)  # ФИО руководителя (контактного лица)
    # description = models.TextField()  # Краткого описания, которое заполняется в WYSIWYG редакторе
    description = RichTextField(blank=True, null=True)  # Краткого описания, которое заполняется в WYSIWYG редакторе
    created_date = models.DateField(auto_now_add=True)  # Даты создания записи
    change_date = models.DateTimeField(auto_now=True)  # Даты изменения записи
    address = models.CharField(max_length=254)  # Адрес
    phone_number = models.ManyToManyField('PhoneNumber')  # Телефон (несколько); +38-(0__)-__-___-__
    e_mail = models.ManyToManyField('Email')  # E-mail (несколько);

    class Meta:
        ordering = ['name_company']
        verbose_name_plural = 'Customer`s'

    def __str__(self):
        return f'{self.name_company}; {self.created_date}; {self.description[:60:]}'


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.phone_number


class Email(models.Model):
    e_mail = models.EmailField()

    def __str__(self):
        return self.e_mail
