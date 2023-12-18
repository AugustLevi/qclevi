"""Quizpj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from quizapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.register,name='signup'),
    path('category/',views.category_list,name='categorylist'),
    path('quiz/<int:category_id>/',views.quiz_detail, name='category_detail'),
    path('quizoption/', views.quiz, name='quiz'),
    path('score/',views.score,name='score'),
    path('signout/',views.signout,name='signout'),
    path('review/', views.review, name='review'),
    # re_path(r'^.*/$',views.error_page),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
