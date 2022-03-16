from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Link con las views basadas en funciones qeu trae django ::: http://ccbv.co.uk/

# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#     })


# def detail(request, question_id): # Son páginas basadas en funciones, function base views
#     question = get_object_or_404(Question, pk=question_id)   # get_object_or_404, función que nos eleve error 404 si no encuentra la pregunta
#     return render(request, "polls/detail.html", {
#         "question": question
#     })


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#     })

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]  # -pub_date con un menos al incio, indica que se organiza de la más reciente a la más antigua

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:  # En try except, el else significa, si todo salió bien, haga lo que está en el else
        selected_choice.votes += 1  # Se suma un voto
        selected_choice.save()      # Se guarda en la base de datos
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))  # Redirige a otro página, a results, reverse es lo mismo que url en el archivo html
