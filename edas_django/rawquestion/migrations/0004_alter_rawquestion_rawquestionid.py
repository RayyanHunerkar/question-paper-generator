# Generated by Django 4.0.5 on 2022-06-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawquestion', '0003_alter_rawquestion_rawquestionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawquestion',
            name='rawquestionID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]