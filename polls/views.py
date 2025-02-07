from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# from django.template import loader # Since i'm using render() shortcut
# '''
# render() - is a very common idiom to load a template, fill a context
# and return Httpresponse object with the results of the rendered template

# The render() function takes the request object as its first 
# argument, a template name as its second, and a dictionary as its optional
# 3rd arguments. It returns an Httpresponse object of the given template with the
# context.
# '''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

# '''shortcut: get_object_or_404()
# It's a very common idiom to use get() and raise Http404 if the object does
# not exist.
# The get_object_or_404() function takes a django model as its first argument
# and an arbitrary number of keyword arguments, which it passes to the get() 
# function of the model manager. it raises Http404 if the object doesn't eixst.
# '''
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)