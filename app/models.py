from django.db import models


class City(models.Model):
    name = title = models.CharField(max_length=100)

    class Meta:
        db_table = "city"                   
        verbose_name = "Город"
        verbose_name_plural = "Города"

class Street(models.Model):
    name = title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город')


    class Meta:
        db_table = "street"
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"


class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город')
    street =  models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name='улица')
    house_number = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        db_table = "shop"
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
