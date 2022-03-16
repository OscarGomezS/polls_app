from django.urls import path

from . import views  # El punto significa que se está importando de la carpeta actual (en este caso, polls)


app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    #ex: /polls/5/
    path("<int:pk>/detail/eslamejorpagina", views.DetailView.as_view(), name="detail"),
    #ex: /polls/5/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # <int:question_id>/results/ ... es la forma de pasar párametros a la función mediante la url
    #ex: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]