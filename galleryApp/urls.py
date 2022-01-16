from django.urls import path
from . import views
# http://127.0.0.1:8000/galleryApp/photoworks/
# http://127.0.0.1:8000/galleryApp/videoworks/
app_name = 'galleryApp' #设置应用名
urlpatterns = [
    path('photoworks/',views.photoworks,name='photoworks'), #照片
    path('videoworks/',views.videoworks,name='videoworks'), #视频
]