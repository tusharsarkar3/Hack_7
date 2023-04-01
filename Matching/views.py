from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import *
from django.contrib.auth.models import User
from Matching.models import *
from social.urls import *
from django.contrib.auth.decorators import login_required


def questions(request):
    if request.method=="POST":  
            dob = request.POST.get('dobu')
            tob = request.POST.get('timeu')
            pob = request.POST.get('placeu')
            state = request.POST.get('stateu')
            city = request.POST.get('cityu')
            age = request.POST.get('ageu')
            partner_age_low = int(request.POST.get('agep').strip(" ").split("-")[0])
            partner_age_high = int(request.POST.get('agep').strip(" ").split("-")[1])
            gender = request.POST.get('genderu')
            partner_gender = request.POST.get('genderp')
            religion = request.POST.get('religionu')
            partner_religion = request.POST.get('religionp')
            mothertongue = request.POST.get('mothertongueu')
            partner_mothertongue = request.POST.get('mothertonguep')
            relationshiptype = request.POST.get('relationshiptypeu')
            edu = request.POST.get('eduu')
            partner_edu = request.POST.get('edup')
            profession = request.POST.get('profu')
            partner_profession = request.POST.get('profp')
            datechar = request.POST.get('pref1')
            animal = request.POST.get('pref2')
            daynight = request.POST.get('pref3')
            movie = request.POST.get('pref4')
            music = request.POST.get('pref5')
            minmax = request.POST.get('pref6')
            MBTI = request.POST.get('mbtiEI') + request.POST.get('mbtiSN') + request.POST.get('mbtiTF') + request.POST.get('mbtiJP')
            interests = request.POST.get('inthobu')
            print(MBTI)
            questions = Questions.objects.create(user=request.user,dob =dob,tob=tob,pob=pob,state=state,
                                                 city=city,age=age,partner_age_low=partner_age_low,
                                                 partner_age_high=partner_age_high,gender=gender,
                                                 partner_gender=partner_gender,religion=religion,
                                                 partner_religion=partner_religion,mothertongue=mothertongue,
                                                partner_mothertongue=partner_mothertongue,relationshiptype=relationshiptype,
                                                edu=edu,partner_edu=partner_edu,profession=profession,
                                                partner_profession=partner_profession,
                                                datechar=datechar,animal=animal,daynight=daynight,movie=movie,
                                                music=music,minmax=minmax,MBTI=MBTI,interests=interests)
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
    # matches=User.objects.all()
    matches = Matches.objects.filter(user=request.user)
    return render(request, 'Matching/show_matches.html',context={'matches':matches})

@login_required
def swipeCard(request,pk):
    if request.POST.get('action') == '':
        match = Matches.objects.get(pk=pk)
        if (request.POST.get('swipe')=='left'):
            match.swiped_left = True
        else:
            match.swiped_right = True
        match.save()
        return redirect('show_matches')
    else:
        return redirect('show_matches')