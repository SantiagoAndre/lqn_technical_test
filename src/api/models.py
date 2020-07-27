from django.db import models
from django.utils.translation import gettext_lazy as _

class Character(models.Model):
    name = models.CharField(_("name"),max_length=100)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = _('character')
        verbose_name_plural = _('characters')




class Planet(models.Model):
    name = models.CharField(_("name"),max_length=100)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = _('planet')
        verbose_name_plural = _('planets')


class Productor(models.Model):
    name = models.CharField(_("name"),max_length=100)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = _('productor')
        verbose_name_plural = _('productors')




class Movie(models.Model):
    name = models.CharField(_("name"),max_length=100)
    year = models.IntegerField(_("name"))
    director = models.CharField(_("director"),max_length=100)
    opening_crawl =models.CharField(_("opening_clawl"),max_length=500)
    productors = models.ManyToManyField(Productor,verbose_name=_("productors"),blank=True)
    characters = models.ManyToManyField(Character,verbose_name=_("characters"),blank=True)
    planets = models.ManyToManyField(Planet,verbose_name=_("planets"),blank=True)
    @property
    def detail(self):
        return '''
Movie: {0}
{1}
Director: {2}
Productors:
\t{3}
Planets:
\t{4}
'''.format(self.name,self.opening_crawl,self.director,"\n\t".join(map(str,self.productors.all())),"\n\t".join(map(str,self.planets.all())))

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')

