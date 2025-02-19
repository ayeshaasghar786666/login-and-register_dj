from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from .forms import My_Form
from .models import My_Model
# Create your views here.

def add(request):
    st = My_Model.objects.all()
    if request.method == 'POST':
        fm = My_Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = My_Form()
    else:
        fm = My_Form()
    
    return render(request,'add.html',{'form':fm,'stu':st})

def delete(request,id):
    if request.method == 'POST':
        fm = My_Model.objects.get(pk=id)
        fm.delete()
        
    else:
        fm = My_Form()
    return redirect('add')

def update(request, id):
    if request.method == 'POST':
        sm = My_Model.objects.get(pk=id)
        fm = My_Form(request.POST,instance=sm)
        if fm.is_valid():
            fm.save()
            return redirect('add')
        fm = My_Form()
    else:
        sm = My_Model.objects.get(pk=id)
        fm = My_Form(instance=sm)
    return render(request,'update.html',{'form':fm})
        



def register(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            return HttpResponse('PASS1 AND PASS2 ARE NOT EQUAL!')
        else:
            if User.objects.filter(username = uname).exists():
                return HttpResponse('Username already exist! Please enter the different Username. ')
            user = User.objects.create_user(username=uname,email=email,password=pass1)
            user.save()
            return redirect('login')
    return render(request,'register.html')


def login(request):
    message = ""
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user = User.objects.filter(username=uname)
        if user.exists() and user[0].check_password(password):
            authenticated_user = authenticate(request, username=uname, password=password)
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
                return redirect('add')
        else:
            message = "Invalid Username Or Password! Please enter the correct Username or Password."

    return render(request, 'login.html', {'message': message})
