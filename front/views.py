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
	return render(request, "socio/index-socio.html")

def solicitarConsulta(request):
	return render(request, "socio/solicitar-consulta.html")

def vizualizarConsultasAgendadas(request):
	return render(request, "socio/vizualizar-consultas-agendadas.html")

def realizarDoacao(request):
	return render(request, "socio/realizar-doacao.html")

def vizualizarDoacoesRealizadas(request):
	return render(request, "socio/vizualizar-doacoes-realizadas.html")