from django.shortcuts import render, redirect

def index(request):
	return render(request, "index.html")

def consulta(request):
	return render(request, "consulta.html")

def login(request):
	return render(request, "login.html")

def criarConta(request):
	return render(request, "criar-conta.html")



############# ------------ SOCIO ----------------- ##########
def indexSocio(request):
	return render(request, "index-socio.html")