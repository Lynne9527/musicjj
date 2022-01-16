from django.urls import path
from . import views
# http://127.0.0.1:8000/albumsApp/albums/
app_name = 'albumsApp' #设置应用名
urlpatterns = [
    path('albums/',views.albums,name='albums'), #专辑
]