from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index_america', views.index_america, name='index_america'),
    path('brasil', views.brasil, name='brasil'),
    path('canada', views.canada, name='canada'),
]