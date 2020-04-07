from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice
# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('encuestas/index.html')
	context = { 'latest_question_list' : latest_question_list}
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("No existe la pregunta")
	return render(request, 'encuestas/detalle.html', {'question':question})

def results(request, question_id):
	response = "Estas mirando los resultados de las preguntas %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Estas votando en la pregunta: %s." %question_id)