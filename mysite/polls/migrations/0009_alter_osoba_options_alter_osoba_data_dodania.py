# Generated by Django 4.1 on 2023-10-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(verbose_name='data dodania'),
        ),
    ]