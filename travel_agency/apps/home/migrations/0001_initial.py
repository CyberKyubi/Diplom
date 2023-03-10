# Generated by Django 4.1.7 on 2023-03-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('IT', 'Италия'), ('CH', 'Швейцария'), ('FR', 'Франция'), ('IE', 'Ирландия'), ('JP', 'Япония'), ('NO', 'Норвегия')], max_length=2, verbose_name='Страна')),
                ('country_image', models.ImageField(upload_to='img/products/', verbose_name='Каталог')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
    ]