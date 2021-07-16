from django.urls import path
from .views import KategoriListView, KategoriCreate, KategoriUpdate, KategoriDestroye, KategoriRetrive, \
    SherbimUpdate,SherbimCreate, SherbimRetrive,SherbimiListView,SherbimDestroye, \
    ShtimSherbimiRetrive, ShtimSherbimiCreate, ShtimSherbimiDestroye, ShtimSherbimiUpdate, ShtimSherbimiListView
urlpatterns = [
    #kategori
    path('kategori/', KategoriListView.as_view()),
    path('add/', KategoriCreate.as_view()),
    path('kategori/<int:pk>/delete/', KategoriDestroye.as_view()),
    path('kategori/<int:pk>/view/', KategoriRetrive.as_view()),
    path('kategori/<int:pk>/update/', KategoriUpdate.as_view()),

    #Lloj_Sherbimi
    path('', SherbimiListView.as_view()),
    path('add/', SherbimCreate.as_view()),
    path('<int:pk>/view/', SherbimRetrive.as_view()),
    path('<int:pk>/update/', SherbimUpdate.as_view()),
    path('<int:pk>/delete/', SherbimDestroye.as_view()),

    #Shto Sherbim
    path('shto/', ShtimSherbimiCreate.as_view()),
    path('liste/', ShtimSherbimiListView.as_view()),
    path('<int:pk>/view/', ShtimSherbimiRetrive .as_view()),
    path('<int:pk>/update/', ShtimSherbimiUpdate.as_view()),
    path('<int:pk>/delete/', ShtimSherbimiDestroye.as_view()),
]