# Generated by Django 4.0.5 on 2022-06-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawquestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawquestion',
            name='unit',
            field=models.IntegerField(),
        ),
    ]
