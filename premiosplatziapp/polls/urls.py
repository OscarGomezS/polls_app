from django.urls import path

from . import views  # El punto significa que se está importando de la carpeta actual (en este caso, polls)

urlpatterns = [
    path("", views.index, name="index")
]