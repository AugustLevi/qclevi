from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def str(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    option1 = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='media/', blank=True, null=True)
    option2 = models.CharField(max_length=100)
    image2 = models.ImageField(upload_to='media/', blank=True, null=True)
    option3 = models.CharField(max_length=100)
    image3 = models.ImageField(upload_to='media/', blank=True, null=True)
    option4 = models.CharField(max_length=100)
    image4 = models.ImageField(upload_to='media/', blank=True, null=True)
    correct_option = models.CharField(max_length=100)

    def str(self):
        return self.content

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.user.username} - {self.category.name} - {self.score}"

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField(default=None)

    def str(self):
        return f"{self.user} - {self.comments}"

    

    
