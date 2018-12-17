from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import *
import bcrypt
def index(request):
    context = {}
    return render(request, 'drego/index.html', context)

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode('utf-8'), user[0].password.encode('utf-8'))
        if is_pass:
            request.session['id'] = user[0].id
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/')
    else:
        messages.error(request, "User does not exist")
    return redirect('/')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        DOB = request.POST['DOB']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(first_name=first_name, last_name=last_name, email=email, DOB=DOB, password=hashed_pw)
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def register_page(request):
    return render(request, 'drego/register.html')

def login_page(request):
    return render(request, 'drego/login.html')

def weeks(request):
    weeks = Week.objects.all()
    context = {
        "weeks": weeks
    }
    return render(request, 'drego/weeks.html', context)

def games(request, week_id):
    week = Week.objects.get(id=week_id)
    games = Game.objects.filter(week=week)
    context = {
        "week": week,
        "games": games,
    }
    return render(request, 'drego/games.html', context)

def single_game(request, week_id, game_id):
    week = Week.objects.get(id=week_id)
    game = Game.objects.get(id=game_id)
    context = {
        "week": week,
        "game": game,
    }
    return render(request, 'drego/single-game.html', context)

def plans(request):
    plans = Plan.objects.all()
    context = {
        "plans": plans
    }
    return render(request, 'drego/plans.html', context)
