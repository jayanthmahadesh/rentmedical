from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .templates.forms import createuserform
from django.contrib.auth import authenticate,login as auth_login,logout
# Create your views here.
from .models import category,subproducts
from django.contrib import messages
from django.http import HttpResponse



def home(request):
    cat = category.objects.all()

    return render(request,'accounts/home.html',{'cat':cat})
def register(request):


    if(request.user.is_authenticated):
         return redirect('home')
    else:
        form = createuserform()
        if(request.method=='POST'):
            form = createuserform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'registration successfull')
                return redirect('login')
            
                
        context={'form':form}
        return render(request,'accounts/register.html',context)


def login(request):
        if(request.user.is_authenticated):
            return redirect('home')
        else:
            if request.method=='POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request,username=username,password=password)
                if(user is not None):
                        auth_login(request,user)
                        request.session['userid'] = user.id
                        request.session['useremail'] = user.email
                        print(user.email)
                        print(user.id)



                        return redirect('/')
                else:
                        messages.info(request,'username or password is incorrect')
            context={}
            
            return render(request,'accounts/login.html',context)
def logoutuser(request):
    logout(request)
    return redirect('login')

def products(request,productid):

    subpros = subproducts.objects.filter(subproductskey=productid)
    context={
        'subpros':subpros
    }

    return render(request,'accounts/products.html',context)
def details(request,uniqueproid):

     displaypro = subproducts.objects.filter(uniqueproductid=uniqueproid)

     context={
          'pros':displaypro
     }
    
    
     return render(request,'accounts/details.html',context)
def order(request,uniqueproid):
    product = subproducts.objects.filter(uniqueproductid=uniqueproid)
    context ={
         'pros':product
    }
    return render(request,'accounts/orderform.html',context)