from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
    name = models.CharField('Ime', max_length=100)
    description = models.CharField('Opis', max_length=350)

    class Meta:
        verbose_name = 'Kategorija'
        verbose_name_plural = 'Kategorije'

    def __unicode__(self):
        return '%s' % (self.name,)

    def __str__(self):
        return '%s' % (self.name,)


class Post(models.Model):
    title = models.CharField('Naslov', max_length=100)
    sub_title = models.CharField('Podnaslov', max_length=100, blank=True, null=True)
    lead = RichTextField('Lead')
    content = RichTextField('Vsebina')
    category = models.ForeignKey(Category, null=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True)

    class Meta:
        verbose_name = 'Objava'
        verbose_name_plural = 'Objave'

    def __unicode__(self):
        return '%s' % (self.title,)

    def __str__(self):
        return '%s' % (self.title,)

