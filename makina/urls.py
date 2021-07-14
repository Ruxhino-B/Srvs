from django.urls import path
from .views import Lloj_makineSerializersListView, MakineCreate, MakineSerializerListView, VariantMakineSerializersListView, \
    MakineDestroy, MakineRetrive, MakineUpdate, VariantMakineCreate, VariantMakineDestroy, VariantMakineRetrive, VariantMakineUpdate, \
    Lloj_makineDestoy, Lloj_makineRetrive, LlojMakineCreate, Lloj_makineUpdate

urlpatterns = [

    #Makina
    path('', MakineSerializerListView.as_view()),
    path('add/', MakineCreate.as_view()),
    path('<slug:pk>/view/', MakineRetrive.as_view()),
    path('<slug:pk>/delete/', MakineDestroy.as_view()),
    path('<slug:pk>/update/', MakineUpdate.as_view()),

    #Variant Makine
    path('varianti/', VariantMakineSerializersListView.as_view()),
    path('varianti/add/', VariantMakineCreate.as_view()),
    path('varianti/<int:pk>/view/', VariantMakineRetrive.as_view()),
    path('varianti/<int:pk>/delete/', VariantMakineDestroy.as_view()),
    path('varianti/<int:pk>/update/', VariantMakineUpdate.as_view()),

    #Lloj_Makine
    path('lloji/', Lloj_makineSerializersListView.as_view()),
    path('lloji/create/', LlojMakineCreate.as_view()),
    path('lloji/<int:pk>/view/', Lloj_makineRetrive.as_view()),
    path('lloji/<int:pk>/delete/', Lloj_makineDestoy.as_view()),
    path('lloji/<int:pk>/update/', Lloj_makineUpdate.as_view()),

]