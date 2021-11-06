from django.urls import path
from .views import PunonjesListVeiew, PunonjesCreate, PunonjesDestroy, PunonjesUpdate, PunonjesRetrive, \
    RoliListVeiw, RoliCreate, RoliUpdate, RoliDestroy
urlpatterns = [
    path('',PunonjesListVeiew.as_view()),
    path('add/', PunonjesCreate.as_view()),
    path('<int:pk>/view/', PunonjesRetrive.as_view()),
    path('<int:pk>/delete/', PunonjesDestroy.as_view()),
    path('<int:pk>/update/', PunonjesUpdate.as_view()),
    path('roli/', RoliListVeiw.as_view()),
    path('roli/add/', RoliCreate.as_view()),
    path('roli/<int:pk>/update/',RoliUpdate.as_view()),
    path('roli/<int:pk>/delete/', RoliDestroy.as_view())
]