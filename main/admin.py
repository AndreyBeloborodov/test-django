from django.contrib import admin
from .models import Emotion, Question

admin.site.register(Question)
admin.site.register(Emotion)
