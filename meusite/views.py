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
    conectar = sqlite3.connect("db.sqlite3")
    cursor = conectar.execute("SELECT * FROM meusite_loot WHERE email = ?;", (usuario,))

    for x in cursor:
        usuario_check = str(x[1])
        senha_check = str(x[2])
        print(usuario_check)
        print(senha_check)

        if usuario == usuario_check and senha == senha_check:
            return render(requests, "logado/index.html")
        else:
            return render(requests, "login/index.html")

    cursor.close()
    conectar.close()

    ip = requests.META.get("REMOTE_ADDR")
    logar_ip = logip(ip=ip)
    logar_ip.save()

    return render(requests, "login/index.html")
