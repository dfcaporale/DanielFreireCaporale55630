from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader #imports templates loader

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def probando_template1(self):

	## Hard way:
	#miHtml = open("C:/Users/danie/Dropbox/_coderhouse/2023/Python/entregas/TerceraPreEntrega_DanielFreireCaporale/WorldTickets/WorldTickets/Templates/template1.html")
	#template = Template(miHtml.read())
	#myContext = Context()
	#document = template.render(myContext)

	## Easy way:
	dictionary = dict()
	dictionary['names'] = ['Jhon', 'Jake', 'Michael']

	template = loader.get_template('template1.html') # uso cargadores
	document = template.render(dictionary) #contexto ahora DEBE ser un diccionario
	
	return HttpResponse(document)