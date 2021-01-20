from django.shortcuts import render, redirect

def init(request):
	return render(request, "consulta.html")
