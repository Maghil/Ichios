from django.shortcuts import render
from django.http import HttpResponse
from homepage.forms import UploadForm, SearchForm
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from homepage.models import Adetails
from datetime import datetime
from django.conf import settings
import hashlib
import os
from .validators import validateSoundAssets


def index(request):
   # Ignore error below pylint Runs good...! ;)
    data = Adetails.objects.all()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)


def upload(request):
    if request.method == "POST":
        uf = UploadForm(request.POST, request.FILES)
        if uf.is_valid():
            if (validateSoundAssets(uf.cleaned_data['filename'])):
                name = uf.cleaned_data['name']
                description = uf.cleaned_data['description']
                tags = uf.cleaned_data['tags']
                filename = uf.cleaned_data['filename']
                now = datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                hash_value = name+description+tags+date_time
                result = hashlib.md5(hash_value.encode())
                Adetails(name=name, description=description, tags=tags,hash_value=result.hexdigest(), files=filename).save()
                messages.success(
                    request, "Your File was submitted successfully...!")
                context = {
                    'form': UploadForm()
                }
                return render(request, 'upload.html', context)
            else:
                context = {
                    'form': UploadForm()
                }
                messages.error(request, "Explicit content detected or harmul file content")
                return render(request, 'upload.html', context)
        else:
            context = {
                'form': UploadForm()
            }
            messages.error(request, "Invalid File or format !")
            return render(request, 'upload.html', context)
    else:
        context = {
            'form': UploadForm()
        }
        return render(request, 'upload.html', context)

def search(request):
    uf = SearchForm(request.POST)
    if request.method == "POST":
        if uf.is_valid():
            name = uf.cleaned_data['search']
            res = Adetails.objects.filter(
                Q(name__icontains=name) | Q(tags__icontains=name)
            )
            context = {
                'data': res,
                'form': uf
            }
            return render(request, 'search.html', context)

    else:
        # Ignore error below pylint Runs good...! ;)
        data = Adetails.objects.all()
        context = {
            'data': data,
            'form': uf
        }
        return render(request, 'search.html', context)
