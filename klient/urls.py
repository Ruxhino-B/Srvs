from django.urls import path
from .views import KlientListView, KlientRetrive, KlientListDelete, KlientUpdate
urlpatterns = [
    path('', KlientListView.as_view()),
    path('<int:pk>/view/', KlientRetrive.as_view()),
    path('<int:pk>/delete/', KlientListDelete.as_view()),
    path('<int:pk>/update/', KlientUpdate.as_view()),
]