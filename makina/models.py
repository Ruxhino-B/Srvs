import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
nr_sediljesh_choises = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9')
]
nr_dyersh_choises = [
    ('2/3','2/3'),
    ('4/5','4/5'),
    ('6/7','6/7')
]
karburanti_choises = [
    ('Benzin','Benzin'),
    ('Nafte','Nafte'),
    ('Gaz-Benzin','Gaz-Benzin'),
    ('Hibrid','Hibrid'),
    ('Elektrik','Elektrik'),
    ('Tjeter','Tjeter')
]
kapaciteti_choises = [
    ('1000','1000'),
    ('1200','1200'),
    ('1300','1300'),
    ('1400','1400'),
    ('1500','1500'),
    ('1600','1600'),
    ('1800','1800'),
    ('2000','2000'),
    ('2200','2200'),
    ('2400','2400'),
    ('2500','2500'),
    ('2700','2700'),
    ('3000','3000'),
    ('3200','3200'),
    ('4000','4000'),
    ('4500','4500'),
    ('5000','5000'),
    ('5500','5500'),
    ('6000','6000'),
    ('6500','6500'),
    ('7000','7000'),
    ('8000','8000'),
    ('9000','9000')
]
transmisioni_choises=[
    ('Manual','Manual'),
    ('Automatik','Automatik'),
    ('Gjysem-Automatik','Gjysem-Automatik')
]
njyra_choises=[
    ('kuqe','kuqe'),
    ('blu','blu'),
    ('zeze','zeze'),
    ('bardhe','bardhe'),
    ('jeshil','jeshil'),
    ('gri','gri'),
    ('verdhe','verdhe')
]
tip_makine_choices = [
    ('Sedan','Sedan'),
    ('Kupe','Kupe'),
    ('Smart','Smart'),
    ('Furgon','Furgon'),
    ('Kamion','Kamion'),
    ('Kabriolet','Kabriolet'),
    ('Foristrade','Foristrade')
]
class Lloj_Makine(models.Model):
    emer = models.CharField(max_length=50)
    def __str__(self):
        return self.emer

class Variant_Makine(models.Model):
    emer = models.CharField(max_length=50)
    lloi_makines = models.ForeignKey(Lloj_Makine, on_delete=models.CASCADE)
    def __str__(self):
        return self.emer


class Makina (models.Model):
    shasia = models.CharField(primary_key=True, null=False, blank=False, max_length=20)
    targa = models.CharField(max_length=10, blank=False, null=False)
    lloji = models.ForeignKey(Lloj_Makine, on_delete=models.CASCADE)
    varianti = models.ForeignKey(Variant_Makine, on_delete=models.CASCADE)
    tipi = models.CharField(choices=tip_makine_choices, max_length=20, default='Sedan')
    viti_prodhimi = models.IntegerField(default=2008, validators=[MaxValueValidator(datetime.date.today().year), MinValueValidator(1800)])
    nr_sediljesh = models.CharField(choices=nr_sediljesh_choises, max_length=50)
    nr_dyersh = models.CharField(choices=nr_dyersh_choises, max_length=50)
    kilometra = models.PositiveIntegerField()
    karburanti = models.CharField(choices=karburanti_choises, max_length=50)
    kapaciteti = models.CharField(choices=kapaciteti_choises, max_length=50)
    transmisioni = models.CharField(choices=transmisioni_choises, max_length=50)
    ngjyra = models.CharField(choices=njyra_choises, max_length=50)
    kualidimi = models.DateField(blank=False, null=False)
    siguracioni = models.DateField(blank=False, null=False)
    date_regjistrimi = models.DateField(auto_now=True)
    #

    def __str__(self):
        return self.lloji.emer + ' ' + self.targa



# from makina.script.load_makina import run
# run()
# from makina.script.variant_makine import run
# run()
from makina.script.shto_makina import  shto_makine
#shto_makine()