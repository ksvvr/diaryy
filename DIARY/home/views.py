from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Entry
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

@login_required(login_url="homelogin")
def about(request):
    return render(request,'about.html')    


@login_required(login_url="homelogin")
def view_entries(request):
    user_entries = Entry.objects.filter(user=request.user)
    return render(request, 'read.html', {'user_entries': user_entries})


@login_required(login_url="homelogin")
def read(request):
    objects = Entry.objects.filter(user=request.user)
    l1=list()
    for i in objects:
       l1.append(i)
    context = {'l1': l1}
    return render(request, 'read.html', context)

@login_required(login_url="homelogin")
def write(request):
    return render(request,'write.html')

def loginUser(request):
    if request.method == "POST" :
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('Invalid Credentials... <a href="">Retry</a>')

        #if user in User.objects.filter(username=username):
        #pass
    else:    
        return redirect('homelogin')
    

def signupUser(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        name=request.POST['name']
        email=request.POST['email']

        if password==password1:
            if User.objects.filter(username=username).exists():
                return HttpResponse('<h1>Username Already Exists! , Try a New One...</h1><a href="/signup">Retry</a>')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=name,email=email)
                user.save()
                msg="SignUp was Successfull"
                return render(request,'home.html',{'msg':msg})   
        else:
            return HttpResponse('Passwords Didnot Match ,<a href="/signup"> Try Again </a>')
    else:    
        redirect('login')

@login_required(login_url="homelogin")
def index(request):
    user=request.user
    return render(request,'index.html',{'user':user})

def logoutUser(request):
    logout(request)
    return redirect('homelogin')

@login_required(login_url="homelogin")
def create_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('diary')
        user = request.user
        entry = Entry.objects.create(title=title, content=content, user=user)
        # do something with the new entry, like redirect to its detail page
        # return redirect('entry_detail', pk=entry.pk)
        entry.save()
        return HttpResponse('Entry Successful...  <a href="/write">Go Back</a>')
    else:
        # render the form
        return redirect(request,'write')

