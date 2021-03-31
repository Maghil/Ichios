from django.shortcuts import render
from django.http import HttpResponse
from homepage.forms import UploadForm, SearchForm
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from homepage.models import Adetails
from ichiosManaged.models import statistics_oneword,logs,recent
from ichiosManaged.views import logging_ctx
from datetime import datetime
from django.db.models import F
from django.conf import settings
import hashlib,datetime
import os
from .validators import validateSoundAssets


def index(request):
    data = Adetails.objects.all()
    context = {
        'data': data
    }
    ## stats for visit
    if statistics_oneword.objects.filter(id=1).exists():
        statistics_oneword(id=1,visiters=F('visiters')+1,reports=F('reports'),upload=F('upload'),logs=F('logs')).save()
    else:
        statistics_oneword(visiters=1).save()
    ##End

    #logs
    logging_ctx("Ichios - Request","User accessing the site by this IP "
    + get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
    #End logs

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
                now = datetime.datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                hash_value = name+description+tags+date_time
                result = hashlib.md5(hash_value.encode())
                Adetails(ip=get_client_ip(request),name=name, description=description, tags=tags,hash_value=result.hexdigest(), files=filename).save()
                messages.success(
                    request, "Your File was submitted successfully...!")
                context = {
                    'form': UploadForm()
                }
                #recent
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                recent(ip=get_client_ip(request),action="Upload",datetxt=str(datetime.datetime.now().date()),
                timetxt=str(current_time),name=name,filepath=filename).save()
                ##

                ##statistics for upload
                if statistics_oneword.objects.filter(id=1).exists():
                    statistics_oneword(id=1,visiters=F('visiters'),reports=F('reports'),upload=F('upload')+1,logs=F('logs')).save()
                else:
                    statistics_oneword(upload=1).save()
                ##End
                
                #logs
                logging_ctx("Ichios FileUpload - Success","User uploaded file "+name +" the site by this IP "
                + get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
                    #End logs

                return render(request, 'upload.html', context)
            else:
                context = {
                    'form': UploadForm()
                }
                messages.error(request, "Explicit content detected or harmul file content")
               
                ##statistics for upload
                if statistics_oneword.objects.filter(id=1).exists():
                    statistics_oneword(id=1,visiters=F('visiters'),reports=F('reports')+1,upload=F('upload'),logs=F('logs')).save()
                else:
                    statistics_oneword(reports=1).save()
                ##End

                #logs
                logging_ctx("Ichios FileUpload - Failed","User uploaded file was rejected due to restrictions the site , IP "
                + get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
                #End logs
                return render(request, 'upload.html', context)
        else:
            context = {
                'form': UploadForm()
            }
            #logs
            logging_ctx("Ichios FileUpload - Failed","User upload Data invalid, IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
            #End logs
            messages.error(request, "Invalid File or format !")
            return render(request, 'upload.html', context)
    else:
        context = {
            'form': UploadForm()
        }
        #logs
        logging_ctx("Ichios FileUpload - Access","User accessed the page by this IP "
        + get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
        #End logs
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
            #recent
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            recent(ip=get_client_ip(request),action="Search",datetxt=str(datetime.datetime.now().date()),
            timetxt=str(current_time),name=name,filepath="Null").save()
            ##

            ##statistics for upload
            if statistics_oneword.objects.filter(id=1).exists():
                statistics_oneword(id=1,visiters=F('visiters'),reports=F('reports'),upload=F('upload'),logs=F('logs')+1).save()
            else:
                statistics_oneword(logs=1).save()
            ##End
            
            #logs
            logging_ctx("Ichios Search - Request","User requested to search "+name+"  by this IP "
            + get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
            #End logs

            return render(request, 'search.html', context)

    else:
        data = Adetails.objects.all()
        context = {
            'form': uf,
            'typehint':"type something in search"
        }
        #logs
        logging_ctx("Ichios Search - Access","User Accessed this page by this IP "
        + get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
        #End logs
        return render(request, 'search.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return str(ip)
