from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib import auth
from django.shortcuts import redirect

def search_name(request,user):
    try:
        user = User.objects.get(username=user)
        
        print(model_to_dict(user))
        return HttpResponse(f"Search result for name:{user},email:{user.email}")
    except:
        return HttpResponse("No user here.ok!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def useradd(request,name):
    try:
        user = User.objects.get(username=user)
        return HttpResponse("User already exists")
    except:
        user = User.objects.create_user(name,"text@aloha.com","9876")
        user.first_name = "Chang"
        user.last_name = "yang"
        user.is_staff = False
        user.is_active = True
        user.save()
        return HttpResponse(f"{user.username} 帳號新增成功<a href='/login/'>登入</a>")
    
def login(request):
    if request.method=="POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        # print(f"ID:{name},PW:{password}")
        user = auth.authenticate(username = name,password = password)
        # print(user)
        if user:
            auth.login(request,user)
            return redirect("/index/?status=0")
        else:
            return redirect("/index/?status=2")
    else:    
        return render(request,'login.html')   

def index(request):
    message = "" 
    status_message = {
        "0" : "登入成功",
        "1" : "帳號未啟用",
        "2" : "帳號或密碼錯誤"
    }
    if 'status' in request.GET:
        status = request.GET['status']
        message = status_message.get(status, "")
    return render(request, 'index.html', {"message":message})
def longout(request):
    auth.logout(request)
    return redirect("/index/")