from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_america, name='index_america'),
    path('indexAmerica', views.index_america, name='index_america'),
    path('brasil', views.brasil, name='brasil'),
    path('canada', views.canada, name='canada'),
]