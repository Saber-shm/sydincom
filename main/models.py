from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Administrateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank = True)
    last_name = models.CharField(max_length=120, blank = True)
    phone_number = models.CharField(max_length=120, blank = True)
    email = models.EmailField(blank = True)



class Residence(models.Model):
    adress = models.CharField(max_length=500)
    name = models.CharField(max_length=120, blank = True)
    balance = models.CharField(max_length= 120,blank = True)

class Propriétaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120, blank = True)
    email = models.EmailField(blank = True)

class Propriéter(models.Model):
    adress = models.CharField(max_length=120)
    propriéter_type = models.CharField(max_length=120,choices= (("propriéter","Propriéter") ,("loyer","Loyer")))
    propriétaire = models.ForeignKey(Propriétaire, on_delete=models.CASCADE)
    residence = models.OneToOneField(Residence,on_delete=models.CASCADE)
    description = models.TextField(blank = True)


    
