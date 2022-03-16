import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):         # POr sintanxis de POO va como singular y con capital. Esto corresponde
    # al nombre de la tabla, también llamdaos modelos
    # El id no se requiere crear 
    question_text = models.CharField(max_length=200)     # Viene de un VarChar de la base de datos
    pub_date = models.DateTimeField("date published")     # Viene de un DATETIME de la base de datos

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # on_delete  elmina todas las preguntas
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)       # Contador que empieza en cero y se incrementa

    def __str__(self):
        return self.choice_text
