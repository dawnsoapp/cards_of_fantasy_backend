import datetime
from django.db import models
# import django.utils import timezone

# Create your models here.
class Question(models.Model):
    user = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    upvote = models.IntegerField(default=0)
    def to_dict(self):
        return {
            "user": self.user,
            "message": self.message,
            "upvote": self.upvote
        }
        
        
    

class Score(models.Model):
    score_name = models.CharField(max_length=12)
    score_num = models.IntegerField(default=0)
    score_time = models.TimeField(default=0)
    def to_dict(self):
        return {
            "score_name": self.score_name,
            "score_num": self.score_num,
            "score_time": self.score_time
        }