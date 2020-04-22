from django.shortcuts import render,HttpResponse,redirect ,HttpResponseRedirect
from .forms import *
import requests
import PIL
# Create your views here.
def index(request):
   
    return render(request,'style/homepage.html')


def stylee(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            content_image=form.cleaned_data.get("content_image")
            style_image= form.cleaned_data.get("style_image")
            
            r = requests.post("https://api.deepai.org/api/neural-style",
            files={'style': style_image,
            'content': content_image,},
            headers={'api-key': '8becf283-308b-4452-aa32-4216d037d95e'})
            context={}
            context['processed']=r.json
           

            

            return render(request,'style/result.html',{'context':context})
        else:
            return HttpResponse('Invalid')
    else:
        form=ImageForm()

    return render(request,'style/main.html',{'form':form})



def about(request):
    return render(request,'style/about.html')