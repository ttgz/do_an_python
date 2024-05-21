from django.shortcuts import render
from django.http import HttpResponse
from . import app_tai_video
import pytube
# Create your views here.

def index(request):
    statusDownload = False
    if(request.method=='POST'):
        videoDownload = {
            "url": "",
            "resolution":"",
        }
        req = request.POST
        for key, value in req.items():
            if(key=="url"):
                videoDownload['url'] = value
            if(key=="resolution"):
                videoDownload['resolution'] = value
        statusDownload = app_tai_video.download_youtube_video(videoDownload['url'],videoDownload['resolution'])
        if(statusDownload == True):
            yt = pytube.YouTube(videoDownload['url'])
            return render(request,'pages/home.html',{'statusDownload':statusDownload,'titleVideo':yt.title})   
        else:
            return render(request,'pages/home.html',{'statusDownload':False})     
    return render(request,'pages/home.html')
