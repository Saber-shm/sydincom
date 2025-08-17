from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings   
urlpatterns = [
    path("",dashboard_page, name = "admin_dashboard_page" ),
    path("test",test_s, name = "test"),
    path("liste_de_biens/<residence_id>", liste_de_bien, name = "liste_de_biens")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
