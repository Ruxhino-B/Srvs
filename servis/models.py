
from django.db import models
import datetime

from django.utils import timezone

from klient.models import Klient
from sherbim.models import Shto_Sherbim
# Create your models here.


def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

cmimi_shto_sherbim = Shto_Sherbim.cmimi

class Rezervim(models.Model):

    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    date_fillimi = models.DateTimeField(default=datetime.datetime.now())
    date_mbarimi = models.DateTimeField(default=one_day_hence())
    sherbim1 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim1')
    sherbim1 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim2')
    sherbim2 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim3')
    sherbim3 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim4')
    sherbim4 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim5')
    sherbim5 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim6')
    sherbim6 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim7')
    sherbim7 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim8')
    sherbim8 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim9')
    sherbim9 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True, related_name='shrbim0')
    cmimi = models.DecimalField(decimal_places=2, max_digits=9999999)

    def __str__(self):
        return self.klient.emer + ' ' + self.klient.mbiemer