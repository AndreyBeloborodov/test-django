from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
    
    
class Question(models.Model):
    question = models.CharField(max_length = 200)
    answer = models.BooleanField(default = False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Emotion(models.Model):
    emotion = models.CharField(max_length = 200)
    positive = models.BooleanField(default = False)

    def __str__(self):
        return self.emotion

    class Meta:
        verbose_name = 'Эмоция'
        verbose_name_plural = 'Эмоции'

