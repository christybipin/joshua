# Generated by Django 4.2.5 on 2023-09-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todosapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-04-23'),
            preserve_default=False,
        ),
    ]
