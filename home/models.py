from django.db import models
from django.utils import timezone



class UserRegistration(models.Model):
    name = models.CharField(max_length=20)
    class1 = models.CharField(max_length=5)
    Username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    conform = models.CharField(max_length=20)
    is_user = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.Username}"
    
class mini(models.Model):
    caption = models.CharField(max_length=200)
    video1 = models.FileField(upload_to='video1/%y', null=True)

class Animation1(models.Model):
    caption = models.CharField(max_length=200)
    video1 = models.FileField(upload_to='video1/%y', null=True)

class Animation2(models.Model):
    caption2 = models.CharField(max_length=200)
    video2 = models.FileField(upload_to='video2/%y', null=True)

class Minigames1(models.Model):
    heading = models.CharField(max_length=255)
    minigames_file = models.FileField(upload_to='minigames', null=True)

class Minigames2(models.Model):
    heading = models.CharField(max_length=255)
    minigames_file = models.FileField(upload_to='minigames2', null=True)

class Reviews(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Import timezone from django.utils

class Quiz(models.Model):
    title = models.CharField(max_length=255, unique=True)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
# models.py in the home app


from django.contrib.auth.models import User  # You may need to import User

class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s Quiz Score: {self.score}"
