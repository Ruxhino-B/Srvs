from django.urls import path
from .views import RezervimListApi,RezervimCreateApi, RezervimUpdateApi, \
    RezervimRetriveApi, RezervimDestroyApi

urlpatterns = [
    path('', RezervimListApi.as_view()),
    path('<int:pk>/view/', RezervimRetriveApi.as_view()),
    path('<int:pk>/update/', RezervimUpdateApi.as_view()),
    path('<int:pk>/delete/', RezervimDestroyApi.as_view()),
    path('create/', RezervimCreateApi.as_view()),
]