from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the index page of the polls application of the website")


def detail(request,question_id):
    return HttpResponse('This is the detail of question_id {ques_id}'.format(ques_id = question_id))


def results(request, question_id):
    return HttpResponse('This is the results page of question_id {ques_id}'.format(ques_id = question_id))


def vote(request, question_id):
    return HttpResponse('This is the vote page for page question_id {ques_id}'.format(ques_id = question_id))
