from django.shortcuts import render
from django.shortcuts import HttpResponse
#快速测试：是否实现对每个应用页面的访问
def gallery(request):
    html = '<html><body>作品</body><html>'
    return HttpResponse(html)
def photoworks(request):
    html = '<html><body>歌手照片</body><html>'
    return HttpResponse(html)
def videoworks(request):
    html = '<html><body>歌手视频</body><html>'
    return HttpResponse(html)