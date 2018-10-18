
# -*- coding: utf-8 -*-

#from django.shortcuts import render

#Tipos de views fornecidos pelo django
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Importando o reverse_lazy
from django.urls import reverse_lazy

#Importando os models do diretório atual
from . import models

#Importando formulários específicos do arquivo forms.py
from .forms import UUIDUserForm, UUIDUserFormEdit, DisciplinaForm, QuestaoForm

#HomeView
class HomeView(TemplateView):
	template_name = 'home.html'

#UserCreateView
class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'cadastro.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = UUIDUserForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreateView, self).form_valid(form)

#VerPefilView
class Perfil(ListView):
    model = models.UUIDUser
    template_name = 'perfil.html'

#EditarPerfilView
class Perfiledit(UpdateView):
    model = models.UUIDUser
    template_name = 'perfiledit.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = UUIDUserFormEdit
    
#ExcluirPerfilView
class Perfildelete(DeleteView):
    model = models.UUIDUser
    template_name = 'perfildelete.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = UUIDUserFormEdit

#CadastarDisciplinaView
class CadastrarDisciplina(CreateView):
    model = models.Disciplina
    template_name = 'cadastrardisciplina.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = DisciplinaForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.prof = self.request.user
        obj.save()
        return super(CadastrarDisciplina, self).form_valid(form)

#VerDisciplinasView
class SuasDisciplinas(ListView):
    model = models.Disciplina
    template_name = 'suasdisciplinas.html'

#EditarDisciplinaView
class DisciplinaEdit(UpdateView):
    model = models.Disciplina
    template_name = 'disciplinaedit.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = DisciplinaForm
    
#ExcluirDisciplinaView
class DisciplinaDelete(DeleteView):
    model = models.Disciplina
    template_name = 'disciplinadelete.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = DisciplinaForm

#CriarQuestaoView
class CriarQuestao(CreateView):
    model = models.Questao
    template_name = 'criarquestao.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = QuestaoForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.prof = self.request.user
        obj.save()
        return super(CriarQuestao, self).form_valid(form)

#VerQuestoesView
class SuasQuestoes(ListView):
    model = models.Questao
    template_name = 'suasquestoes.html'

#EditarQuestaoView
class QuestaoEdit(UpdateView):
    model = models.Questao
    template_name = 'questaoedit.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = QuestaoForm

#ExcluirQuestaoView
class QuestaoDelete(DeleteView):
    model = models.Questao
    template_name = 'questaodelete.html'
    success_url = reverse_lazy('bancodequestoes:home')
    form_class = QuestaoForm