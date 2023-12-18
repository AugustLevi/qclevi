from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from quizapp.models import Category,Question,UserScore,Reviews
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == "POST":
        image = request.POST.get('image')
        username = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Your passwords didn't match!!")
            return render(request,'signup.html')
        else:
            myuser = User.objects.create_user(username,email,password1)
            myuser.save()
            messages.success(request,"Your account has been successfully created.")
            return redirect('/home/')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print(username,email,password)
        user = authenticate(request, username=username,email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('/signin/')  
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categoryview.html', {'categories': categories})
def quiz_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    questions = Question.objects.filter(category=category)
          
    return render(request, 'quizdetail.html', {'category': category, 'questions': questions})

def quiz(request):
    questions = Question.objects.all()
    score = 0

    if request.method == 'POST':
        for q in questions:
            selected_option = request.POST.get(q.content)
            if selected_option == q.correct_option:
                score += 1

    return render(request,'score.html', {'questions': questions, 'score': score})



def leaderboard(request):
    scores = UserScore.objects.all().order_by('-score', 'date_played')[:10] 
    return render(request, 'leaderboard.html', {'scores': scores})
    
#no leaderboard till now cause of a bunch of errors 

@login_required
def score(request):
    user = request.user
    questions = Question.objects.all()
    score = 0
    reviews = Reviews.objects.all()
    if request.method == 'POST':
        for q in questions:
            selected_option = request.POST.get(q.content)
            if selected_option == q.correct_option:
                score += 1

        total_questions = Question.objects.filter(category=questions.first().category).count()
        percentage = (score / total_questions) * 100
        feedback = get_feedback(percentage)

        category = questions.first().category
        UserScore.objects.create(user=user, category=category, score=score)
        user = request.user
        comments = request.POST.get('comments')
        if comments:
            Reviews.objects.create(user=user,comments=comments)
        # return render(request, 'score.html', {'questions': questions, 'score': score, 'percentage': percentage, 'feedback': feedback,'reviews': reviews})
    return render(request, 'score.html', {'questions': questions, 'score': score,'reviews': reviews})
    
    


def get_feedback(percentage):
    if percentage >= 50:
        return "Well done!"
    elif 50 <= percentage < 30:
        return "Good effort."
    else:
        return "Keep going."

def review(request):
    reviews = Reviews.objects.all()

    return render(request, 'reviews.html', {'reviews': reviews})