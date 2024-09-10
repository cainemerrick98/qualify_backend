from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.TextField()
    users = models.ManyToManyField(User)

class QuestionType(models.Model):
    TEXT = 'tx'
    CATEGORY = 'ct'
    types = {
        TEXT: 'Text',
        CATEGORY:'Category'
    }
    _type = models.TextField(choices=types)

class Question(models.Model):
    question = models.TextField()
    _type = models.ForeignKey(QuestionType)

#TODO: maybe remove the questionaire object and just allow teams to have a set of questions they refine over time?
class Questionairre(models.Model):
    team = models.ForeignKey(Team)
    questions = models.ManyToManyRel(Question)

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.deletion.CASCADE)
    response = models.TextField()

class ResponseChange(models.Model):
    response = models.ForeignKey(Response)
    previous_value = models.TextField()
    new_value = models.TextField()
    user = models.ForeignKey(User)

class Qualification(models.Model):
    questionairre = models.ForeignKey(Questionairre)
    responses = models.ManyToOneRel(Response)

class Opportunity(models.Model):
    name = models.TextField()
    stage = models.TextField()
    qualification = models.ForeignKey(Qualification, default=None)




