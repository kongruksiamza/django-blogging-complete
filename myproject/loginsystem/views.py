from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,"backend/login_register.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]
        if username == "" or email == "" or password=="" or repassword=="":
            messages.info(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("member")
        else:
            if password == repassword :
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username นี้มีคนใช้แล้ว")
                    return redirect("member")
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"อีเมลนี้เคยลงทะเบียนไปแล้ว")
                    return redirect("member")
                else:
                    user=User.objects.create_user(
                        username = username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.info(request,"สร้างบัญชีเรียบร้อย")
                    return redirect("member")
            else:
                messages.info(request,"ไม่สามารถลงทะเบียนได้รหัสผ่านไม่ตรงกัน")
                return redirect("member")

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect("panel")
    else:
        messages.info(request,"ไม่พบข้อมูลบัญชีผู้ใช้")
        return redirect("member")

def logout(request):
    auth.logout(request)
    return redirect('member')