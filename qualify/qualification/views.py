from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from rest_framework import permissions
from models import Team, User, Opportunity, Qualification, Question, Questionairre, QuestionType, Response, ResponseChange 
from serializers import TeamSerializer, OpportunitySerializer, QualificationSerializer, QuestionairreSerializer, QuestionSerializer, ResponseSerializer, UserSerializer
# Create your views here.

class TeamView(CreateAPIView, UpdateAPIView, RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permissions_classes = []

class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = []

class OpportunityView(CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permissions_classes = []

class QualificationView(CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permission_classes = []

class QuestionairreView(CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Questionairre.objects.all()
    serializer_class = QuestionairreSerializer
    permission_classes = []

class QuestionView(CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = []

class QuestionTypeView(ListAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionType
    permission_classes = []

class ResponseView(CreateAPIView, UpdateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = []
