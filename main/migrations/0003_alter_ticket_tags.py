# Generated by Django 3.2.9 on 2021-11-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ticket_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tags',
            field=models.ManyToManyField(to='main.Tag'),
        ),
    ]