from django.urls import path
from api import views

urlpatterns = [
    path("ciphers/", views.ciphers_list),
    path("encrypt/", views.encrypt),
    path("decrypt/", views.decrypt),
]