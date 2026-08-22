from django.urls import path
from api import views

urlpatterns = [
    path("ciphers/", views.ciphers_list),
]