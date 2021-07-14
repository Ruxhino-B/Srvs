from django.urls import path
from .views import PunonjesListVeiew, PunonjesCreate, PunonjesDestroy, PunonjesUpdate, PunonjesRetrive
urlpatterns = [
    path('',PunonjesListVeiew.as_view()),
    path('add/', PunonjesCreate.as_view()),
    path('<int:pk>/view/', PunonjesRetrive.as_view()),
    path('<int:pk>/delete/', PunonjesDestroy.as_view()),
    path('<int:pk>/update/', PunonjesUpdate.as_view())
]