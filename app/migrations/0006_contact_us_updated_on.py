# Generated by Django 4.1.5 on 2023-02-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]