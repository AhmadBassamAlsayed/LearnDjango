from django.db import models
import datetime
from django.utils import timezone as time

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published",default=time.now())
    def __str__(self):
        return (self.question_text)
    def was_published_recently(self):
        return self.pub_date>=time.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return (self.choice_text)

