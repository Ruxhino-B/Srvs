import csv
from makina.models import Lloj_Makine, Variant_Makine

def run():
    fopen = open(r'C:\Users\Ruxhino\PycharmProjects\djangoProject\makina\script\Volkswagen.csv')
    lexues = csv.reader(fopen)
    AC = Lloj_Makine.objects.get(id=113)
    for row in lexues:
        if Variant_Makine.objects.filter(emer=row[0]).count() == 0:
            Variant_Makine.objects.create(emer=row[0], makina=AC)

