import csv

from makina.models import Lloj_Makine


def run():
    fopen = open(r'C:\Users\Ruxhino\PycharmProjects\djangoProject\makina\script\lloj_makine.csv')
    lexues = csv.reader(fopen)
    #Lloj_Makine.objects.all().delete()
    for row in lexues:
        print(row[0])

        Lloj_Makine.objects.create(emer_lloi=row[0])
