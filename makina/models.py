from django.db import models

# Create your models here.
YEAR_IN_SCHOOL_CHOICES = [
    ('AC', 'AC'),
    ('Acura', 'Acura'),
    ('Aixam', 'Aixam'),
    ('Alfa Romeo', 'Alfa Romeo'),
    ('Abarth', 'Abarth'),
    ('ALPINA', 'ALPINA'),
    ('Artega', 'Artega'),
    ('Asia Motors', 'Asia Motors'),
    ('Aston Martin', 'Aston Martin'),
    ('Audi', 'Audi'),
    ('Austin', 'Austin'),
    ('Austin Healey', 'Austin Healey'),
    ('BAIC', 'BAIC'),
    ('Bentley', 'Bentley'),
    ('BMW', 'BMW'),
    ('Borgward', 'Borgward'),
    ('Brilliance', 'Brilliance'),
    ('Bugatti', 'Bugatti'),
    ('Buick', 'Buick'),
    ('Cadillac', 'Cadillac'),
    ('Casalini', 'Casalini'),
    ('Abarth', 'Abarth'),
    ('Abarth', 'Abarth'),
    ('Abarth', 'Abarth'),


]
class Makina (models.Model):
    shasia = models.UUIDField(primary_key=True, null=False, blank=False, max_length=17)
    targa = models.CharField(max_length=10)
    lloji = models.Choices