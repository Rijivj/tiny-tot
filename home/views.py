from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import UserRegistration
from .models import *
from .forms import ReviewForm, UserRegistrationForm

def index(request):
    return render(request, 'index.html')

def rock(request):
    return render(request, 'rock.html')

def first(request):
    return render(request, 'first.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserRegistration.objects.filter(Username=username, password=password).first()
        
        if user:
            # Set the session variable 'class1'
            request.session['class1'] = user.class1

            if user.class1 in ['pre-kg', 'lkg', 'ukg', '1']:
                print("Redirecting to home1")
                return redirect('home1')
            elif user.class1 in ['2', '3', '4', '5']:
                print("Redirecting to home2")
                return redirect('home2')
            else:
                print("Invalid class:", user.class1)
        else:
             return HttpResponse("No user available")
        
    return render(request, 'login.html')

from django.db import IntegrityError

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        class1 = request.POST['class1']
        username = request.POST['username']
        password = request.POST['password']
        conform = request.POST['conform']

        if password == conform:
            user = UserRegistration(name=name, class1=class1, Username=username, password=password, conform=conform, is_user=True) 
            if UserRegistration.objects.filter(class1=class1):
                user.save()
                return redirect('login')
            
        else:
            return HttpResponse("Passwords do not match")

    return render(request, 'register.html')


def home2(request):
    return render(request, 'home2.html') 

def home1(request):
    return render(request, 'home1.html') 

def game1(request):
    return render(request,'game1.html') 

def hangmangame(request):
    return render(request,'hangmangame.html')

def memory(request):
    return render(request,'memory.html') 


def egggame(request):
    return render(request,'egggame.html') 

def animation1(request):
    dict_docs = { 
        'animation1': Animation1.objects.all()
    }
    return render(request,'animation1.html', dict_docs) 

def animation2(request):
    dict_docs = { 
        'animation2': Animation2.objects.all()
    }
    return render(request,'animation2.html', dict_docs) 

def minigames1(request):
    dict_docs = { 
        'minigames1': Minigames1.objects.all()
    }
    return render(request,'minigames1.html', dict_docs) 

def minigames2(request):
    dict_docs = { 
        'minigames2': Minigames2.objects.all()
    }
    return render(request,'minigames2.html', dict_docs) 

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('add_review')
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'user': request.user})


def display_reviews(request):
    reviews = Reviews.objects.all()  # Assuming Review is the model for reviews
    return render(request, 'display_reviews.html', {'reviews': reviews})

def quiz_view(request):
    # Assuming you want to display a specific quiz, you can fetch it here
    quiz = Quiz.objects.first()  # Change this logic based on your requirements
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        # Handle form submission and calculate score
        # This is a simplified example; you might want to add more logic here
        score = 0
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}', None)
            if selected_choice_id:
                selected_choice = Choice.objects.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1

        return render(request, 'result.html', {'score': score, 'quiz': quiz})

    return render(request, 'quiz.html', {'quiz': quiz, 'questions': questions})
