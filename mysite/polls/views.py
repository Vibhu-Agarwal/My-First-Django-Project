from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.


def index(request):
    questions = Question.objects.order_by('pub_date')[:5]
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    return HttpResponse('This is the results page of question_id {ques_id}'.format(ques_id = question_id))


def vote(request, question_id):
    return HttpResponse('This is the vote page for page question_id {ques_id}'.format(ques_id = question_id))
