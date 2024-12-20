from django.shortcuts import render,redirect
from main.models import *
# Create your views here.


def dashboard_page(request):
    if request.user.is_authenticated:
        residences = Residence.objects.all()
        
        return render(request, "admin_dashboard.html",{"residences": residences,"num_residences": len(residences)})
    else:
        return redirect("login_page")


