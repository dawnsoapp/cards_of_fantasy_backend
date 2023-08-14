from django.shortcuts import render
from django.http import JsonResponse
from core.models import Question, Score
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

# Create your views here.

#CREATE
def post_question(request):
    if request.method == "POST":
        question_object = Question.objects.all()
        question = Question.to_dict(question_object)
        return JsonResponse(question)

#READ
def read_questions(request):
    if request.method == "GET":
        questions = Question.objects.all()
        question_list = [question.to_dict(questions) for question in questions]
        return JsonResponse(question_list)
