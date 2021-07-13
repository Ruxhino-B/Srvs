import csv
from makina.models import Lloj_Makine, Variant_Makine, Makina

def shto_makine():
    fopen = open(r'C:\Users\Ruxhino\PycharmProjects\djangoProject\makina\script\shto-makina.csv', encoding='utf-8-sig')
    lexues = csv.reader(fopen)
    for row in lexues:
        lloj_makine = Lloj_Makine.objects.filter(emer=row[2]).first()
        variant_makine = Variant_Makine.objects.filter(emer=row[3]).first()
        if Makina.objects.filter(shasia=row[0]).count() == 0:
            Makina.objects.create(shasia=row[0],targa=row[1], lloji=lloj_makine, varianti=variant_makine, tipi=row[4], nr_dyersh=row[5], nr_sediljesh=row[6], kilometra=row[7], karburanti=row[8],kapaciteti=row[9], transmisioni=row[10], ngjyra=row[11], kualidimi=row[12], siguracioni=row[13])