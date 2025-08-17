from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings  
urlpatterns = [
    path('add_residence', add_residence, name='add_residence'),
    path("add_bien_step_1", add_bien_etape_1, name = "add_bien_step1"),
    path("add_bien_step_2", add_bien_etape_2,name = "add_bien_step2")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
