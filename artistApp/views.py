from django.shortcuts import render
from django.shortcuts import HttpResponse
#快速测试：是否实现对每个应用页面的访问
def artist(request):
    html = '<html><body>歌手</body><html>'
    return HttpResponse(html)
def singerSurvey(request):
    html = '<html><body>歌手概况</body><html>'
    return HttpResponse(html)
def singerHonor(request):
    html = '<html><body>歌手荣誉</body><html>'
    return HttpResponse(html)