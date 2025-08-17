from django.shortcuts import render,redirect
from main.models import *
from .forms import *
# Create your views here.


def add_residence(request):

    if request.user.is_authenticated:
        account_type = None
        user_is_syndicat = False
        user_is_propriétaire = False
        user_is_admin = False
        try:
            try: 
                account_type = Administrateur.objects.get(user = request.user)
                user_is_admin = True
            except:
                account_type = Syndicat.objects.get(user = request.user)
                user_is_syndicat = True
        except:
            account_type = Propriétaire.objects.get(user = request.user)
            user_is_propriétaire = True

        form = ResidenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
        return render(request,"add_residence.html", {"user_is_admin": user_is_admin, "user_is_syndicat": user_is_syndicat, "user_is_propriétaire": user_is_propriétaire,"form": form})

    else:
        return redirect("home_page")
    
def add_bien_etape_1(request):
    if request.user.is_authenticated:
        admin = Administrateur.objects.get(user = request.user)
        propriétaires = Propriétaire.objects.all()
        print(propriétaires[0].user.last_login)
        return render(request,"add_bien_step_1.html", {"propriétaires": propriétaires})
    


def add_bien_etape_3(request):
    if request.user.is_authenticated:
        admin = Administrateur.objects.get(user = request.user)
        form = PropriéterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
        return render(request, "add_bien.html", {"form": form})

def add_bien_etape_2(request):
    if request.user.is_authenticated:
        admin = Administrateur.objects.get(user = request.user)
        residences = Residence.objects.all()
        return render(request,'add_bien_step_2.html',{"residences":residences})
    


