from django.shortcuts import redirect, render

from django.contrib.auth import login,logout,authenticate

from user.forms import CustomUserForm
from . models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db import transaction

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,"user/home.html")


def logout_user(request):
    logout(request)
    return redirect('login')



def create_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():

            try:
                # all the database operations within the with transaction.atomic() block are treated 
                # as a single transaction. If any of the database operations fail (raises an exception)
                # , the transaction will be rolled back, and no changes will be persisted to the 
                # database.

                with transaction.atomic():
                    user=form.save(commit=False)
                    user.set_password(form.cleaned_data['password'])
                    user.save()


                    #create phone instance
                    phone=Phone(user=user,phone=form.cleaned_data['phone'])
                    phone.save()
                    return redirect('home')

            except Exception as e:
                messages.error(request,e)
                return redirect('create_user')

        else:
            messages.error(request,form.errors)
    else:
        form= CustomUserForm()
    return render(request,'user/create.html',{'form':form})


def login_user(request):

    user = None
    
    if request.method == 'POST':
        username_phone_email = request.POST['username_phone_email']
        password = request.POST['password']
        

        try:

            #if username
            user = authenticate(request,username=username_phone_email,password=password)
            print(1," ",user)
            if user is not None:
                login(request,user)
                return redirect('home')

            
            
            #not username / check with phone
            #first exception is handled by backend and return None
            #but when accessing with phone it's like that 
            #so another try except is needed

            user=Phone.objects.get(phone=username_phone_email).user

            print(2," ",user)
            user=authenticate(request,username=user.username,password=password)
            
            
            
            
        except ObjectDoesNotExist:
                    
                    try:
            
                         #not username , phone / check with email
                        user=User.objects.get(email=username_phone_email)

                        print(3," ",user)

                        user=authenticate(request,username=user.username,password=password)

                        
                
                    except ObjectDoesNotExist:
                
                        messages.error(request,"User does not exist")
                        return redirect('login')
        
    if user is not None:
        login(request,user)
        return redirect('home')
            
    return render(request,
                    "user/login.html")
