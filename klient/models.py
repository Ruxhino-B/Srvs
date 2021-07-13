from django.db import models
from makina.models import Makina

# Create your models here.
class Klient(models.Model):
    emer = models.CharField(max_length=50)
    mbiemer = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    makina = models.ForeignKey(Makina, on_delete=models.CASCADE)
    date_regjistrimi = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.emer + ' ' + self.mbiemer + ' ' + self.makina.targa