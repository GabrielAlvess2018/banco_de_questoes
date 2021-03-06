
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
from .forms import UUIDUserForm, UUIDUserFormEdit, DisciplinaForm, QuestaoForm, ProvaForm, RepostaForm

#HomeView
class HomeView(TemplateView):
	template_name = 'home.html'

#UserCreateView
class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'cadastro.html'
    success_url = reverse_lazy('bancodequestoes:login')
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
    success_url = reverse_lazy('bancodequestoes:perfil')
    form_class = UUIDUserFormEdit
    
#ExcluirPerfilView
class Perfildelete(DeleteView):
    model = models.UUIDUser
    template_name = 'perfildelete.html'
    success_url = reverse_lazy('bancodequestoes:perfil')
    form_class = UUIDUserFormEdit

#CadastarDisciplinaView
class CadastrarDisciplina(CreateView):
    model = models.Disciplina
    template_name = 'cadastrardisciplina.html'
    success_url = reverse_lazy('bancodequestoes:suasdisciplinas')
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
    success_url = reverse_lazy('bancodequestoes:suasdisciplinas')
    form_class = DisciplinaForm
    
#ExcluirDisciplinaView
class DisciplinaDelete(DeleteView):
    model = models.Disciplina
    template_name = 'disciplinadelete.html'
    success_url = reverse_lazy('bancodequestoes:suasdisciplinas')
    form_class = DisciplinaForm

#CriarQuestaoView
class CriarQuestao(CreateView):
    model = models.Questao
    template_name = 'criarquestao.html'
    success_url = reverse_lazy('bancodequestoes:suasquestoes')
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
    success_url = reverse_lazy('bancodequestoes:suasquestoes')
    form_class = QuestaoForm

#ExcluirQuestaoView
class QuestaoDelete(DeleteView):
    model = models.Questao
    template_name = 'questaodelete.html'
    success_url = reverse_lazy('bancodequestoes:suasquestoes')
    form_class = QuestaoForm

#ListDisciplinasView
class ListDisciplina(ListView):
    model = models.Disciplina
    template_name = 'criarprova.html'

#QuestaoDisciplinaView
class QuestaoDisciplina(DetailView):
    model = models.Disciplina
    template_name = 'questoesdisciplina.html'
    def get_context_data(self, **kwargs):
        kwargs['questoes'] = models.Questao.objects.all()
        return super(QuestaoDisciplina, self).get_context_data(**kwargs)

#CriarQuestaoView
class CriarprovaView(CreateView):
    model = models.Prova
    template_name = 'criarquestaoview.html'
    success_url = reverse_lazy('bancodequestoes:verprovas')
    form_class = ProvaForm

    def get_form_kwargs(self):
        kwargs = super(CriarprovaView, self).get_form_kwargs()
        kwargs['user'] = self.request.user # pass the 'user' in kwargs
        return kwargs

    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.prof = self.request.user
        obj.save()
        return super(CriarprovaView, self).form_valid(form)
    

#VerProvasViews
class VerProvas(ListView):
    model = models.Prova
    template_name = 'verprovas.html'

#ProvaEditView
class ProvaEdit(UpdateView):
    model = models.Prova
    template_name = 'provaeditform.html'
    success_url = reverse_lazy('bancodequestoes:verprovas')
    form_class = ProvaForm

#ProvaDeleteView
class ProvaDelete(DeleteView):
    model = models.Prova
    template_name = 'provadeleteform.html'
    success_url = reverse_lazy('bancodequestoes:verprovas')
    form_class = ProvaForm

#ResponderProvaView
class ResponderProva(CreateView):
    model = models.Resposta
    template_name = 'responderprova.html'
    success_url = reverse_lazy('bancodequestoes:verprovas')
    form_class =  RepostaForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.prof = self.request.user
        obj.save()
        return super(ResponderProva, self).form_valid(form)