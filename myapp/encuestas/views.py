from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'encuestas/resultados.html', {'question': question})

def form(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'encuestas/formulario.html', {'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render (request, 'encuestas/formulario.html', {'question':question, 'error_message': "No elegiste una opcion",})	
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('encuesta:results', args=(question.id,)))

def choice_vote(request,question_id,choice_id):
	question = get_object_or_404(Question, pk=question_id)
	choice = get_object_or_404(Choice, pk=choice_id)
	choice.votes += 1
	choice.save()
	#choice.votes = choice_vote +1
	print("Votaste en: "+choice.choice_text)
	print(choice.votes)
	return detail(request,question_id)

def home(request):
	return render(request, 'encuestas/base.html')