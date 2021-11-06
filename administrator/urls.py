from django.urls import path
from .views import ShtimSherbimiPaAprovuarListView, ShtimSherbimiPaPaguarListView
urlpatterns = [
    path('listepaaprovuar', ShtimSherbimiPaAprovuarListView.as_view()),
    path('listpapaguar', ShtimSherbimiPaPaguarListView.as_view()),

]