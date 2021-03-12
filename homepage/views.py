from django.shortcuts import render
from django.http import HttpResponse
from homepage.forms import UploadForm 
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from homepage.models import Adetails
from datetime import datetime
from django.conf import settings
import hashlib,os
# Create your views here.
def index(request):
   #Ignore error below pylint Runs good...! ;)
    data = Adetails.objects.all()
    context = {
      'data':data
    }
    return render(request,'index.html',context)

def upload(request):
  if request.method == "POST":
    uf = UploadForm(request.POST,request.FILES)
    if uf.is_valid():
      name =uf.cleaned_data['nm']
      des =uf.cleaned_data['des']
      tgs =uf.cleaned_data['tgs']
      flnm =uf.cleaned_data['flnm']
      now = datetime.now()
      date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
      hv   = name+des+tgs+date_time
      result = hashlib.md5(hv.encode()) 
      Adetails(name=name,desc=des,tags=tgs,hahv=result.hexdigest(),files=flnm).save()
      messages.success(request,"Your File was submitted successfully...!")
      context ={
      'form':UploadForm()
      }
      return render(request, 'upload.html',context)
    else:
      messages.error(request,"Your File was No submitted (~_~)")
      return render(request, 'upload.html',context)

  else:

    context ={
      'form':UploadForm()
    }
    return render(request, 'upload.html',context)
#S0NICRAGE21