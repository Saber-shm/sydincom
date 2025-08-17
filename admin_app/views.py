from django.shortcuts import render,redirect
from main.models import *
# Create your views here.


def dashboard_page(request):
    if request.user.is_authenticated:
        residences = Residence.objects.all()
        biens = Propriéter.objects.all()
        return render(request, "admin_dashboard.html",{"residences": residences,"num_residences": len(residences), "num_biens": len(biens)})
    else:
        return redirect("login_page")



def test_s(request):
    if request.user.is_authenticated:
        residences = Residence.objects.all()
        
        return render(request, "admin_base.html",{"residences": residences,"num_residences": len(residences)})
    else:
        return redirect("login_page")
    

def liste_de_bien(request,residence_id):
    if request.user.is_authenticated:
        administrateur = Administrateur.objects.get(pk = request.user)
        residence = Residence.objects.get(pk = residence_id)
        biens = Propriéter.objects.find(residence = residence)

        return render(request, "admin_biens_list.html", {"biens": biens, "residence": residence})

