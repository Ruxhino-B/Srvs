from django.urls import path
from .views import KlientListView
urlpatterns = [
        path('', KlientListView.as_view())
    ]