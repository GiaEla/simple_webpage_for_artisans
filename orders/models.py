from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe

from moneytalks import settings


class Product(models.Model):
    name = models.CharField('Ime izdelka', max_length=40)
    img = models.ImageField('Fotografija')
    size = models.CharField('Velikost/količina', max_length=20, null=True, blank=True)
    price = models.DecimalField('Cena v €',  max_digits=8, decimal_places=2)
    month_price = models.DecimalField('Vzdrževanje na mesec v €', max_digits=8, decimal_places=2, null=True, blank=True)
    sold = models.BooleanField('Prodano', default=False)
    description = RichTextField(verbose_name='Opis izdelka', null=True, blank=True)
    short_description = models.CharField('Kratek opis izdelka (max 40 znakov)', max_length=40, null=True, blank=True)

    def fotografija(self):
        return mark_safe('<img src="{0}" style="width:auto; height:200px;" />'.format(settings.MEDIA_URL + str(self.img)))

    class Meta:
        verbose_name = 'Izdelek'
        verbose_name_plural = 'Izdelki'

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
        return '%s' % (self.name)


class Order(models.Model):
    recipient_email = models.CharField('Email naročnika', max_length=260)
    product_fk = models.ForeignKey(Product, verbose_name="Za izdelek:")
    status = models.CharField('Status naročila', max_length=50)
    date = models.DateTimeField("Čas prejema naročila", null=True, blank=True)
    quantity = models.PositiveSmallIntegerField('Količina', default=1)
    comment = models.CharField('Opomba', max_length=500)

    def izdelek(self):
        return mark_safe('<img src="{0}" style="width:auto; height:200px;" />'.format(settings.MEDIA_URL + str(self.product_fk.img)))


    class Meta:
        verbose_name = 'naročilo'
        verbose_name_plural = 'naročila'