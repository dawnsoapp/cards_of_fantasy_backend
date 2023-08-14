from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.post_question, name="question"),
    path("", views.read_questions, name="question"),
]