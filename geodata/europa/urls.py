from django.urls import path
from . import views


urlpatterns = [
    path('index_europa', views.index_europa, name='index_europa'),
    path('italia', views.italia, name='italia'),
    path('franca', views.franca, name='franca'),
    path('alemanha', views.alemanha, name='alemanha'),
]