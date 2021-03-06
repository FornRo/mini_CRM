# Generated by Django 4.0.1 on 2022-01-10 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0002_email_phonenumber_remove_company_e_mail_and_more'),
        ('do_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doproject',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer_info.company'),
        ),
        migrations.AlterField(
            model_name='doproject',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
