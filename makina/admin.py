from django.contrib import admin
from .models import Lloj_Makine, Variant_Makine, Makina
# Register your models here.
admin.site.register(Makina)
admin.site.register(Lloj_Makine)
admin.site.register(Variant_Makine)
