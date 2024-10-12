from django.db import models

# Create your models here.
# models.py
class Question(models.Model):
    category = models.CharField(max_length=100)
    index = models.IntegerField()
    freq = models.FloatField()
    question = models.TextField()
    answer = models.IntegerField()
    explanation = models.TextField()
    reference = models.CharField(max_length=100)

    def __str__(self):
        return f"Qestions {self.id}: {self.index}: {self.question[:50]}"