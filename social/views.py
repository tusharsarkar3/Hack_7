from django.http.response import Http404
from .models import *
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.models import User
from Matching.urls import *
from django.contrib import messages
from django.db.models import Q
from Matching.models import Questions, Matches


@login_required(login_url='login')
def index(request):
    try:
        user_questions = Questions.objects.get(user = request.user)
        all_hashtags = []
        if user_questions.movie is not None:
            movie = user_questions.movie.strip().split(",")
            all_hashtags.extend(movie)
        if user_questions.music is not None:
            music = user_questions.music.strip().split(",")
            all_hashtags.extend(music)
        if user_questions.book is not None:
            book  = user_questions.book.strip().split(",")
            all_hashtags.extend(book)
        # Q(description__contains=5000) | Q(income__isnull=True)
        posts = []
        for hashtag in all_hashtags:
            inter_posts = Post.objects.filter(description__contains=hashtag)
            if len(inter_posts) != 0:
                for inter_post in inter_posts:
                    posts.append(inter_post)
    except:
        pass

    posts = Post.objects.all()
    print(posts)
    all_users = User.objects.exclude(id=request.user.id)
    liked_posts = [i for i in Post.objects.all() if Like.objects.filter(user=request.user, post=i)]
    followed = [i for i in User.objects.all() if Follow.objects.filter(follower=request.user, followed=i)]

    if request.method == 'POST':
        upload_form = UploadImageForm(request.POST, request.FILES)

        if upload_form.is_valid():
            upload_form.instance.user = request.user.profile
            upload_form.save()

            return redirect('index')

    else:
        upload_form = UploadImageForm()

    context = {'upload_form': upload_form, 'posts': posts, 'liked_posts': liked_posts, 'all_users': all_users,
               'followed': followed}

    return render(request, 'social/index.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('social')

    else:
        form = CreateUserForm
        title = 'New Account'

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form': form, 'title': title}
    return render(request, 'social/accounts/registration.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('social')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if len(Questions.objects.filter(user=request.user))==0:
                    return redirect('questions')
                else:
                    return redirect('index')

            else:
                messages.info(request, 'Username or password is incorrect.')

    context = {}
    return render(request, 'social/accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.instance.user = request.user.profile
            comment_form.instance.post = post

            comment_form.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def like(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        new_like = Like(user=user, post=post)
        new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def follow(request, user_id):
    user = request.user
    other_user = User.objects.get(pk=user_id)
    follow = Follow.objects.filter(follower=user, followed=other_user)
    if follow:
        follow.delete()
    else:
        new_follow = Follow(follower=user, followed=other_user)
        new_follow.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def profile(request):
    
    if request.method == 'POST':
        upload_form = UploadImageForm(request.POST, request.FILES)

        if upload_form.is_valid():
            # upload_form.instance.user = request.user.profile
            upload_form.save()

            return redirect('index')

    else:
        upload_form = UploadImageForm()
    
    profile=Questions.objects.filter(user=request.user)
    context = {'upload_form': upload_form,'profile':profile}

    return render(request, 'social/profile.html', context)
    # return render(request, 'social/profile.html')
