from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        return redirect("admin_dashboard_page")
    else:
        return render(request,'template1/landing.html')
    

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print("authenticated")
        if user is not None:
            login(request,user)
            return redirect("home_page")
    return render(request, "template1/sign-in.html", {})



def logout_page(request):
    logout(request.user)
    return redirect("home_page")