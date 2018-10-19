from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid
from datetime import datetime
from django.db import models

# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True

# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

# DisciplinaModel
# - - - - - - - - - - - - - - - - - - -
class Disciplina(models.Model):
    prof = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='disciplina', verbose_name='professor')
    name = models.CharField(max_length=100, verbose_name='nome')
    description = models.TextField(verbose_name='descrição', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'disciplina'
        verbose_name_plural = 'disciplinas'

# QuestaoModel
# - - - - - - - - - - - - - - - - - - -
class Questao(models.Model):
    prof = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='questão', verbose_name='professor')
    subject = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='questão', verbose_name='disciplina')
    enunciation = models.TextField(verbose_name='enunciado') 
    image = models.ImageField(blank=True, verbose_name='imagem')
    alternative1 = models.TextField(verbose_name='alternativa1')
    alternative2 = models.TextField(verbose_name='alternativa2')
    alternative3 = models.TextField(verbose_name='alternativa3')
    alternative4 = models.TextField(verbose_name='alternativa4')
    alternative5 = models.TextField(verbose_name='alternativa5')
    answer = models.CharField(max_length=100, verbose_name='alternativa correta')

    def __str__(self):
        return self.enunciation

    class Meta:
        verbose_name = 'questão'
        verbose_name_plural = 'questões'

# ProvaModel
# - - - - - - - - - - - - - - - - - - -
class Prova(models.Model):
    prof = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='prova', verbose_name='professor')
    title = models.CharField(max_length=100, verbose_name='título')
    question1 = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='prova1', verbose_name='questão1')
    question2 = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='prova2', verbose_name='questão2', blank=True, null=True)
    question3 = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='prova3', verbose_name='questão3', blank=True, null=True)
    question4 = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='prova4', verbose_name='questão4', blank=True, null=True)
    question5 = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='prova5', verbose_name='questão5', blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'prova'
        verbose_name_plural = 'provas'