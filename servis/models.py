#
# from django.db import models
# import datetime
#
# from django.utils import timezone
#
# from klient.models import Klient
# from sherbim.models import Shto_Sherbim
# # Create your models here.
#
# def one_day_hence():
#     return timezone.now() + timezone.timedelta(days=1)
#
#
# class Rezervim(models.Model):
#     klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
#     date_fillimi = models.DateTimeField(default=datetime.datetime.now())
#     date_mbarimi = models.DateTimeField(default=one_day_hence())
#     sherbim1 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim1 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim2 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim3 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim4 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim5 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim6 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim7 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim8 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     sherbim9 = models.ForeignKey(Shto_Sherbim, on_delete=models.CASCADE, null=True, blank=True)
#     cmimi = models.DecimalField(default=0)
