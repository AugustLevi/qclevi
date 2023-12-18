from django.contrib import admin
from quizapp.models import Category,Question,UserScore,Reviews

admin.site.register(Category)

admin.site.register(Question)

admin.site.register(UserScore)

admin.site.register(Reviews)
