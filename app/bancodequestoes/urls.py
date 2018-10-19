from __future__ import unicode_literals

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'bancodequestoes'

urlpatterns = [
	#Home
	path('', views.HomeView.as_view(), name='home'),

	#Cadastro, Login e Logout
	path('cadastro/', views.UserCreateView.as_view(), name='cadastro'),

	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	#Ver, editar e excluir Perfil
	path('perfil/', views.Perfil.as_view(), name='perfil'),

	path('perfiledit/<pk>/', views.Perfiledit.as_view(), name='perfiledit'),

	path('perfildelete/<pk>/', views.Perfildelete.as_view(), name='perfildelete'),

	#Cadastrar Disciplina
	path('disciplina/', views.CadastrarDisciplina.as_view(), name='disciplina'),

	#Ver, editar e excluir Disciplina
	path('suasdisciplinas/', views.SuasDisciplinas.as_view(), name='suasdisciplinas'),

	path('disciplinaedit/<pk>/', views.DisciplinaEdit.as_view(), name='disciplinaedit'),

	path('disciplinadelete/<pk>/', views.DisciplinaDelete.as_view(), name='disciplinadelete'),

	#Criar Questão
	path('criarquestao/', views.CriarQuestao.as_view(), name='criarquestao'),

	#Ver, editar e excluir Questão
	path('suasquestoes/',views.SuasQuestoes.as_view(), name='suasquestoes'),

	path('questaoedit/<pk>/', views.QuestaoEdit.as_view(), name='questaoedit'),

	path('questaodelete/<pk>/', views.QuestaoDelete.as_view(), name='questaodelete'),

	#Criar Prova
	path('disciplinas/', views.ListDisciplina.as_view(), name='disciplinas'),

	path('questoesdisciplina/<pk>/', views.QuestaoDisciplina.as_view(), name='questoesdisciplina'),
	
	path('criarprova/', views.CriarprovaView.as_view(), name='criarprova'),

	#Ver, editar e excluir Prova
	path('verprovas/', views.VerProvas.as_view(), name='verprovas'),

	path('provaedit/<pk>/', views.ProvaEdit.as_view(), name='provaedit'),

	path('provadelete/<pk>/', views.ProvaDelete.as_view(), name='provadelete'),
]