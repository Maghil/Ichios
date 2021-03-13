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
      name =uf.cleaned_data['name']
      description =uf.cleaned_data['description']
      tags =uf.cleaned_data['tags']
      filename =uf.cleaned_data['filename']
      now = datetime.now()
      date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
      hash_value   = name+description+tags+date_time
      result = hashlib.md5(hash_value.encode()) 
      Adetails(name=name,description=description,tags=tags,hash_value=result.hexdigest(),files=filename).save()
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