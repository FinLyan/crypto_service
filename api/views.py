from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from crypto_core.registry import list_ciphers

@api_view(["GET"])
def ciphers_list(request):
    return Response(list_ciphers())