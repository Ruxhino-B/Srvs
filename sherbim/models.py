import datetime

import django
from django.utils import timezone

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from makina.models import Makina, Lloj_Makine, Variant_Makine
from punonjes.models import Punonjes
# Create your models here.

def one_day_hence():
    return timezone.now() + timezone.timedelta(days=100)

class Kategori_Sherbimi(models.Model):
    emer = models.CharField(max_length=250)

    def __str__(self):
        return self.emer

class Lloj_Sherbimi(models.Model):
    choices_lloji_makine = Lloj_Makine.objects.all().values_list('emer','emer')
    choices_variant_makine = Variant_Makine.objects.all().values_list('emer','emer')
    list_choices_lloji_makine = []
    list_variantesh_makine = []
    for lloj in choices_lloji_makine:
        list_choices_lloji_makine.append(lloj)
    for variant in choices_variant_makine:
        list_variantesh_makine.append(variant)
    kategoria = models.ForeignKey(Kategori_Sherbimi, on_delete=models.CASCADE)
    emer = models.CharField(max_length=250)
    lloj_makine = models.CharField(max_length=250, choices=list_choices_lloji_makine)
    variant_makine = models.CharField(max_length=20, choices=choices_variant_makine)
    viti_prodhimi = models.IntegerField(validators=[MaxValueValidator(datetime.date.today().year), MinValueValidator(1800)])
    materiali_perdorur = models.CharField(max_length=250)
    cmimi = models.DecimalField(decimal_places=2, max_digits=99999999)

    def __str__(self):
        return self.emer + ' ' + self.lloj_makine + ' ' + self.variant_makine

class Shto_Sherbim(models.Model):
    sherbim = models.ForeignKey(Lloj_Sherbimi, on_delete=models.CASCADE)
    makina = models.ForeignKey(Makina, on_delete=models.CASCADE)
    date_sherbimi = models.DateField(default=django.utils.timezone.now)
    sherbimi_rradhes = models.DateField(default=one_day_hence())
    makaniku = models.ForeignKey(Punonjes, on_delete=models.CASCADE)
    cmimi = models.DecimalField(decimal_places=2, max_digits=999999)
    paguar = models.BooleanField(default=False)
    verifikuar = models.BooleanField(default=False)
    koha = models.IntegerField(default=0)

    def __str__(self):
        return self.sherbim.emer + ' ' + self.makina.targa