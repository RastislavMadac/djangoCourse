# aplication

from django.urls import path 

from . import views 

 
 

urlpatterns = [ 

    path('', views.index, name='home_page'), 
    path('premiants', views.premieants, name='school_premiants'),

] 