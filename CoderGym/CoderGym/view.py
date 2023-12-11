from django.shortcuts import render
from django.http import HttpResponse

def pag_principal(request):
    return render(request, "index.html")
