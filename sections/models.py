from django.db import models


class Section(models.Model):
    title = models.CharField('Naslov', max_length=25)
    img = models.ImageField('Fotografija')
    content = models.CharField('Vsebina', max_length=10000, null=True, blank=True)
    html_id = models.CharField('Navigacija za Html', max_length=40, default='html_id')

    class Meta:
        verbose_name = 'Del vsebine'
        verbose_name_plural = 'Deli vsebine'

    def __unicode__(self):
        return '%s' % (self.title)

    def __str__(self):
        return '%s' % (self.title)

    def save(self, *args, **kwargs):
        self.html_id = self.title.replace(' ', '_').lower()

        super(Section, self).save(*args, **kwargs)

