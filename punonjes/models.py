from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Roli(models.Model):
    roli = models.CharField(max_length=50)

    def __str__(self):
        return self.roli

class Punonjes(models.Model):
    emer = models.CharField(max_length=50)
    mbiemer = models.CharField(max_length=50)
    roli = models.ForeignKey(Roli, on_delete=models.CASCADE, default=1)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=250, default=None)
    nr_tel = models.CharField(max_length=13)
    date_fillimi = models.DateField(auto_now_add=True)
    pag_aktuale = models.DecimalField(default=300, decimal_places=2, max_digits=99999999)

    def __str__(self):
        return self.emer + ' ' + self.mbiemer
    def save(self, *args, **kwargs):
        if User.objects.filter(username=self.username).count() == 0:
            User.objects.create_user(username=self.username, email=self.email, password=f'{self.emer}{self.mbiemer}')
        super().save(*args, **kwargs)
