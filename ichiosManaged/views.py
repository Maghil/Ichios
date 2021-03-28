from django.shortcuts import render
from ichiosManaged.forms import RegForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from homepage.models import Adetails
from django.contrib.auth.decorators import login_required
from ichiosManaged.models import statistics_oneword,logs,recent
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
            now = datetime.datetime.now()
            logs(l_loc="Ichios Registration - Success",L_Description="User profile was created in the name of "+str(username)+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'],l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()
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
              now = datetime.datetime.now()
              logs(l_loc="Ichios Registration - Failed",L_Description="Name of the user is "
              +str(form.fields['username'])+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'],
              l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()
              #End logs
              return render(request, 'register.html', context)
    else:
      
        context = {
        'form': RegForm()
        }
        #logs
        now = datetime.datetime.now()
        logs(l_loc="Page Access - Ichios Registration",L_Description="Accessing a restricted page Alert...! "
        +",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'],
        l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()
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
                    now = datetime.datetime.now()
                    logs(l_loc="Ichios Login - Success",L_Description="User logoned use this credential name "
                    +username+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'],
                    l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()
                    #End logs
                    return redirect(dashboard)
            else:
                #logs
                now = datetime.datetime.now()
                logs(l_loc="Ichios Login - Failed",L_Description="User try to login using this credential name "
                +username+",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'],
                l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()
                #End logs
                messages.error(request, "Invalid username or password.")
                form = LoginForm()
                return render(request,"login.html",context={"form":form})
        else:
            #logs
            now = datetime.datetime.now()
            logs(l_loc="Ichios Login - Failed",L_Description="Fields are not valid "
            +",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'],
            l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()
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
    now = datetime.datetime.now()
    logs(l_loc="Ichios Admin - Logout",L_Description="User Logout of the system "
    +",by this IP "+ get_client_ip(request)+" ,UserAgent - "+request.META['HTTP_USER_AGENT'],
    l_datetime=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')).save()
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