from django.urls import path

from . import views

app_name = 'encuesta'
urlpatterns = [
	path('', views.index, name='index'),
	path('pregunta/<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.form, name='form'),
	path('<int:question_id>', views.vote, name='vote'),
	path('home',views.home, name='home'),
	path('<int:question_id>/results/', views.results, name='results'),
]