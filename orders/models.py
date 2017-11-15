from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField('Ime izdelka', max_length=40)
    img = models.ImageField('Fotografija')
    size = models.CharField('Velikost', max_length=20)
    price = models.DecimalField('Cena v €',  max_digits=8, decimal_places=2)
    sold = models.BooleanField('Prodano', default=False)

    class Meta:
        verbose_name = 'Izdelek'
        verbose_name_plural = 'Izdelki'