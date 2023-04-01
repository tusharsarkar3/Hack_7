from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import *
from django.contrib.auth.models import User
from Matching.models import *
from social.urls import *
from django.contrib.auth.decorators import login_required


def questions(request):
    if request.method=="POST":  
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            print(request.user)
            questions = Questions.objects.create(user=request.user,age=age,gender=gender)
            print(questions)
            return redirect('show_matches')
    '''form = QuestionsForm
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewprofiles')
    
        #return redirect('social')

    context = {'form': form}'''
    return render(request, 'Matching/questions.html')

@login_required
def show_matches(request):
    matches=User.objects.all()
    # matches = Matches.objects.get(user=request.user)
    return render(request, 'Matching/show_matches.html',context={'matches':matches})