from django.shortcuts import render
from django.http import HttpResponse
from core.models import Question, Score

# Create your views here.
# get_all_questions(["GET"]):
#     pass

def index(request):
    return HttpResponse("Hello, world. You're at the core index.")