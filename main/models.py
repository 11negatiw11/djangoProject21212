from django.db import models


class Item(models.Model):
    name = models.CharField('Название', max_length=64)
    description = models.TextField('Описание')
    price = models.FloatField('Длительость')

    img = models.ImageField('Фото', upload_to='static/images')
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Запись'
        verbose_name_plural= 'Записи'

class Category(models.Model):
    name = models.CharField('Название', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural= 'Категории'


