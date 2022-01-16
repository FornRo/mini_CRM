from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
# from customer_info.models import Company
from do_projects.models import DoProject


CHANNEL = (
    ('c', 'correspondence'),
    ('p', 'phone'),
    ('i', 'company initiative'),
    ('m', 'mail'),
    ('e', 'email'),
)

RATING = (
    ('+5', 'masterpiece'),
    ('+4', 'great'),
    ('+3', 'very good'),
    ('+2', 'good'),
    ('+1', 'not bad'),
    ('0', 'mediocre'),
    ('-1', 'no way'),
    ('-2', 'bad'),
    ('-3', 'terrible'),
    ('-4', 'negligible'),
)


class Cooperation(models.Model):
    project = models.ForeignKey(DoProject, on_delete=models.SET_NULL, null=True)
    name_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    channel_of_usage = models.CharField(max_length=1, choices=CHANNEL, blank=True, default='m')
    rating = models.CharField(max_length=2, choices=RATING, blank=True, default='0')
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.id} | {self.project.id} | {self.project.company.id}'
