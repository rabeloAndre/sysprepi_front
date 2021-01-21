from django.shortcuts import render, redirect

def index(request):
	return render(request, "index.html")

def consulta(request):
	return render(request, "consulta.html")

