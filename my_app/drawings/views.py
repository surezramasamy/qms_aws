from xml.parsers.expat import model
from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from .models import Drawings_2D,Model_Name, Sub_Assembly
from .forms import drgform,drguploadform,LoginForm
import pandas
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required


class HomePageView(ListView):
    model = Drawings_2D
    template_name = 'home.html'
    


def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    error_message=None
    form=LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid:
            username =form.data.get("username")
            password=form.data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if request.GET.get("next"):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect ('home')
            else:
                error_message="Not Authorised to Download or Upload drawings"
    return render(request,'login.html',{'form':form,'error_message':error_message})


@login_required
@permission_required('Permision', raise_exception=True)
def drgupload(request):
    if request.method == 'POST':
        form = drguploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = drguploadform()   

    return render(request, 'drgupload.html', {
        'form': form
    })


@login_required
@permission_required('Permision', raise_exception=True)
def drg(request):
    drg_qs = None
    search_form = drgform(request.POST or None)
            
    if request.method == 'POST':
        Model_Name = request.POST.get('Model_Name')
        Sub_Assembly_Name = request.POST.get('Sub_Assembly_Name')
        drg_qs = Drawings_2D.objects.filter(Model_Name=Model_Name, Sub_Assembly_Name=Sub_Assembly_Name)

    context = {
        'search_form': search_form,
        'drg_qs': drg_qs,


    }
    return render(request, 'drg.html',  context)
