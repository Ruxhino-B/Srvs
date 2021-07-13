from django.urls import path
from .views import PunonjesListVeiew
urlpatterns = [
    path('',PunonjesListVeiew.as_view()),
]