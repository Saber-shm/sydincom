from django.urls import path
from django.conf.urls.static import static
from django.conf import settings    
from .views import *

urlpatterns = [
    path("", home_page, name = "home_page"),
    path("login/", login_page, name = "login_page"),
    path("logout/", logout_page,name = "logout_page")
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
