from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question, Choice
# Create your views here.
def index(request):
	question_list = Question.objects.all()
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('encuestas/index.html')
	context = { 'latest_question_list' : question_list}
	#return HttpResponse(template.render(context, request))
	return render (request, 'encuestas/index.html',context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'encuestas/detalle.html',{'question':question})

def results(request, question_id):
	response = "Estas mirando los resultados de las preguntas %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Estas votando en la pregunta: %s." %question_id)

def choice_vote(request,question_id,choice_id):
	question = get_object_or_404(Question, pk=question_id)
	choice = get_object_or_404(Choice, pk=choice_id)
	choice.votes += 1
	choice.save()
	#choice.votes = choice_vote +1
	print("Votaste en: "+choice.choice_text)
	print(choice.votes)
	return detail(request,question_id)