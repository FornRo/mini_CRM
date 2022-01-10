from django.db import models

from ckeditor.fields import RichTextField
from customer_info.models import Company


class DoProject(models.Model):
    name_project = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['name_project']

    def __str__(self):
        return self.name_project
