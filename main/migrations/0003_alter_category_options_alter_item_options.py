# Generated by Django 4.0.1 on 2022-03-17 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_item_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
    ]