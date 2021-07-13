from django.urls import path
from .views import Lloj_makineSerializersListView, MakineSerializerListView, VariantMakineSerializersListView
urlpatterns = [
    path('lloji/', Lloj_makineSerializersListView.as_view()),
    path('varianti/', VariantMakineSerializersListView.as_view()),
    path('', MakineSerializerListView.as_view())

]