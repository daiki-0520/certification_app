# Generated by Django 3.1.7 on 2021-03-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiences',
            name='description',
            field=models.TextField(default='', max_length=10000),
        ),
    ]
