#coding:utf-8
from __future__ import unicode_literals

#Forms idea
from django import forms

#Outros
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#Importando os models para criar os formulários
from .models import UUIDUser, Disciplina, Questao

# User: create
# - - - - - - - - - - - - - - - - - - -
class UUIDUserForm(forms.ModelForm):
    class Meta:
        model = UUIDUser
        fields = ('username', 'password')
        labels = {
        'username': 'Nome de Usuário',
        'password': 'Senha',
    }
        widgets={
            'password': forms.PasswordInput()
}

#User: edit
# - - - - - - - - - - - - - - - - - - -
class UUIDUserFormEdit(forms.ModelForm):
    class Meta:
        model = UUIDUser
        fields = ('username','password')
        labels = {
        'username': 'Nome de Usuário',
   }

#form Disciplina
# - - - - - - - - - - - - - - - - - - -
class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ('name', 'description')
        label = {
        'name':'Nome da disciplina',
        'description':'Descrição da disciplina',
        }

#form Questão
# - - - - - - - - - - - - - - - - - - -
class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ('subject', 'enunciation', 'alternative1', 'alternative2', 'alternative3', 'alternative4', 'alternative5', 'answer')
        label = {
        'subject':'Disciplina',
        'enunciation':'Enunciado',
        'alternative1':'Primeira Alternativa',
        'alternative2':'Segunda Alternativa',
        'alternative3':'Terceira Alternativa',
        'alternative4':'Quarta Alternativa',
        'alternativa5':'Quinta Alternativa',
        'answer':'Alternativa correta',
    }