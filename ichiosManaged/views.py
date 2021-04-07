from django.shortcuts import render
from ichiosManaged.forms import RegForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from homepage.models import Adetails
from django.contrib.auth.decorators import login_required
from ichiosManaged.models import statistics_oneword,logs,recent,reports
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
import datetime,os
# Create your views here.
def reg(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, "User Registered successfully...!")
            #logs
            logging_ctx("Ichios Registration - Success","User profile was created in the name of "+str(username)+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
            context = {
                 'form': RegForm()
            }
            return render(request,'register.html',context)
        else:
              messages.error(
                    request, "Failed Register User...!")
              context = {
                 'form': RegForm()
            }
              #logs
              logging_ctx("Ichios Registration - Failed","Name of the user is "
              +str(form.fields['username'])+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
              #End logs
              return render(request, 'register.html', context)
    else:
      
        context = {
        'form': RegForm()
        }
        #logs
        logging_ctx("Page Access - Ichios Registration","Accessing a restricted page Alert...! "
        +",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
        #End logs
        return render(request, 'register.html', context)

def logon(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #logs
                    logging_ctx("Ichios Login - Success","User logoned use this credential name "
                    +username+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
                    #End logs
                    return redirect(dashboard)
            else:
                #logs
                logging_ctx("Ichios Login - Failed","User try to login using this credential name "
                +username+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
                #End logs
                messages.error(request, "Invalid username or password.")
                form = LoginForm()
                return render(request,"login.html",context={"form":form})
        else:
            #logs
            logging_ctx("Ichios Login - Failed","Fields are not valid "
            +",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
            #End logs
            messages.error(request, "Invalid username or password.")
            form = LoginForm()
            return render(request,"login.html",context={"form":form})
    else:
        form = LoginForm()
        return render(request,"login.html",context={"form":form})

def dashboard(request):
    statdata = statistics_oneword.objects.all()
    recentUpload = recent.objects.filter(action="Upload").order_by('-id')
    recentSearch = recent.objects.filter(action="Search").order_by('-id')
    context = {
        'ru':recentUpload,
        'rs':recentSearch,
        'stats': statdata
    }
    return render(request,"home.html",context)


def logoutUser(request):
    #logs
    logging_ctx("Ichios Admin - Logout","User Logout of the system "
    +",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'])
    #End logs
    logout(request)
    return redirect(logon)

def logging(request):
    data = logs.objects.all().order_by('-id')
    context = {
        'logs':data
    }
    return render(request,"logs.html",context)

def recentdo(request):
    data = recent.objects.all().order_by('-id')
    context = {
        'rec':data
    }
    return render(request,"recent.html",context)

def content(request):
    data = Adetails.objects.all().order_by('-id')
    context = {
        'data':data
    }
    return render(request,"content.html",context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return str(ip)

def delete_file(request,hash_value):
    data_to_del = Adetails.objects.get(hash_value=hash_value)
    data_to_del.delete()  
    return redirect(content)

def logging_ctx(title,description):
     now = datetime.datetime.now()
     logs(l_loc=title,L_Description=description,l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: *",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def ireports(request):
    data = reports.objects.all().order_by('-id')
    context = {
        'rept':data
    }
    return render(request,"reports.html",context)

def report_save(ttl,action,data):
     today = datetime.datetime.now().date()
     now = datetime.datetime.now()
     current_time = now.strftime("%H:%M:%S")
     reports(title=ttl,action=action,datetxt=today,timetxt=current_time,data=data).save()