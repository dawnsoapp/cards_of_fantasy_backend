from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from core.models import Question, Score

# Create your views here.

#CREATE
def post_question(request):
    if request.method == "POST":
        response_body = (json.loads(request.body))
        question = Question(user=response_body["user"], message=response_body["message"])
        question.save()
        question_object = question.to_dict()
        return JsonResponse(question_object, safe=False)

#READ
# def read_questions(request):
    elif request.method == "GET":
        questions = Question.objects.all()
        question_list = [question.to_dict() for question in questions]
        return JsonResponse(question_list, safe=False)
    

    # response = HttpResponse()
    # response['allow'] = ','.join(['get', 'post', 'put', 'delete', 'options'])
    # return response
