from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from Hotels.settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

import random

#____________________________________________________________________
#____________________Register, Login, Logout_________________________
#____________________________________________________________________

def RegisterPage(request):
    template_name = 'register.html'

    form = UserCreationForm
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.email = request.POST.get("email")
            obj.save()
            emailll = EmailMessage(
                subject = f'Hello {request.POST.get("username")}',
                body = 'Sign up completed succesfully',
                from_email=EMAIL_HOST_USER,
                to = [request.POST.get('email')]
            )
            emailll.send()
            return redirect('login')
        else:
            message = form.errors
    
    context = {
        'message':message,
        'form':form,
    }

    return render(request,template_name,context)
    

def LoginPage(request):
    template_name = 'login.html'

    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message = 'user not found'
    
    context = {'message':message}

    return render(request,template_name,context)


def Logout(request):
    logout(request)
    return redirect('login')
    
#____________________________________________________________________
#____________________________________________________________________
#____________________________________________________________________


   

def MainInfoF(context,title,subtitle):
    context['maininfo'] = MainInfo.objects.get()
    context['aboutstatus'] = AboutStatus.objects.all()
    context['gallery'] = Gallery.objects.all()
    context['subtitle'] = subtitle
    context['title'] = title





def SearchItem(request):
    word = request.GET.get('q')
    loc_q = request.GET.get('l')
    goall = request.GET.get('goall')
    proplisting = PropertyListing.objects.filter(name__icontains = word,adress__icontains = loc_q,goal = goall)
    statusinfo = HomeStatus.objects.all()
    imgcycle = ImageCycle.objects.get()
    properties = Properties.objects.all()
    moreinfo = MoreInfo.objects.all()
    contactagent = ContactAgent.objects.all()
    propertyagents = PropertyAgents.objects.all()
    clientcomments = ClientOpinions.objects.all()
    context = {
        'statusinfo':statusinfo,
        'imgcycle':imgcycle,
        'properties':properties,
        'moreinfo':moreinfo,
        'proplisting':proplisting,
        'contactagent':contactagent,
        'propertyagents':propertyagents,
        'clientcomments':clientcomments,
                }
    MainInfoF(context,'home','')
    

    return render(request,'index.html',context)



class HomeListView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    login_url = '/login/'
    def get(self,request) :
        statusinfo = HomeStatus.objects.all()
        imgcycle = ImageCycle.objects.get()
        properties = Properties.objects.all()
        moreinfo = MoreInfo.objects.all()
        proplisting = PropertyListing.objects.all()
        contactagent = ContactAgent.objects.all()
        propertyagents = PropertyAgents.objects.all()
        clientcomments = ClientOpinions.objects.all()
        context = {
            'statusinfo':statusinfo,
            'imgcycle':imgcycle,
            'properties':properties,
            'moreinfo':moreinfo,
            'proplisting':proplisting,
            'contactagent':contactagent,
            'propertyagents':propertyagents,
            'clientcomments':clientcomments,
                  }
        MainInfoF(context,'home','')
        

        return render(request,self.template_name,context)
        
    

class AboutListView(ListView):
    template_name = 'about.html'
    
    def get(self,request):
        aboutstatus = AboutStatus.objects.all()
        moreinfo = MoreInfo.objects.all()
        contactagent = ContactAgent.objects.all()
        propertyagents = PropertyAgents.objects.all()

        context = {
            'aboutstatus':aboutstatus,
            'moreinfo':moreinfo,
            'contactagent':contactagent,
            'propertyagents':propertyagents,

            }
        MainInfoF(context,'about','About Us')
        

        return render(request,self.template_name,context)
    
class PropertyListView(ListView):
    template_name = 'property-list.html'

    def get(self,request):
        proplisting = PropertyListing.objects.all()
        contactagent = ContactAgent.objects.all()

        context = {
            'proplisting':proplisting,
            'contactagent':contactagent
                  }
        
        MainInfoF(context,'Property List','Property List')

        return render(request,self.template_name,context)


#---------------------------------------------------------
#----------------------????????????-----------------------
#---------------------------------------------------------


    def post(self,request):
        form = AddPropertyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pr_list')
        else:
            print(form.errors)
            form = AddPropertyForm()
        proplisting = PropertyListing.objects.all()
        contactagent = ContactAgent.objects.all()

        context = {
            'proplisting':proplisting,
            'contactagent':contactagent,
            'form':form,
                  }

        return render(request,self.template_name,context)

        
    
    
#---------------------------------------------------------
#----------------------????????????-----------------------
#---------------------------------------------------------


class ContactPage(DetailView):
    template_name = 'contact.html'


    def get(self, request):
        if request.user.is_authenticated:
            name = request.user.username
            email = request.user.email
        else:
            name = ''
            email = ''

        form = ContactForm()

        context = {
            'form':form,
            'name':name,
            'email':email
                  }
        MainInfoF(context,'contact','Contact Us')
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ContactForm()


        context = {
            'form':form,


                  }

        MainInfoF(context,'contact','Contact Us')
        return render(request,self.template_name,context)

