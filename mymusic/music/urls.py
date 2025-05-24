# application file

from django.urls import path 

from . import views 

 
 

urlpatterns = [ 

    path('', views.index), 
    path('<slug:slug>', views.music_detail,name='song_detail'), 

] 