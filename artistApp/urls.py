from django.urls import path
from . import views
# http://127.0.0.1:8000/artistApp/singerSurvey/
# http://127.0.0.1:8000/artistApp/singerHonor/
app_name = 'artistApp' #设置应用名
urlpatterns = [
    path('singerSurvey/',views.singerSurvey,name='singerSurvey'),#歌手概况
    path('singerHonor/',views.singerHonor,name='singerHonor'),   #歌手荣誉
]