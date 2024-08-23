
from django.urls import path
from . import views 
from .views import add_review, display_reviews
from .views import quiz_view


urlpatterns = [
    path('',views.display_reviews,name='display_reviews'),
    path('login/',views.login, name='login'),
    path('register/',views.register,name='register'),
    path('first/',views.first,name='first'),
    path('home1/',views.home1,name='home1'),
    path('animation1/',views.animation1,name='animation1'),
    path('animation2/',views.animation2,name='animation2'),
    path('minigames1/',views.minigames1,name='minigames1'),
    path('minigames2/',views.minigames2,name='minigames2'),
    path('rock/',views.rock,name='rock'),
    path('memory/',views.memory,name='memory'),
    path('game1/',views.game1, name='game1'),
    path('hangmangame/',views.hangmangame, name='hangmangame'),
    path('egggame/',views.egggame, name='egggame'),
    path('home2/',views.home2, name='home2'),
    path('add_review/', add_review, name='add_review'),
    path('quiz/', quiz_view, name='quiz_view'),
    


]














