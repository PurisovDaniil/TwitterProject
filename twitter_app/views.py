from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .models import Post
from django.contrib.auth.models import User
from .forms import RegisterForm


# Create your views here.


def index(request):
    return render(request, 'twitter_app/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = RegisterForm()
    return render(request, 'twitter_app/register.html', {"form":form})

def search_results(request):
    query = request.GET.get('search_input')
    posts = Post.objects.filter(Q(title__icontains = query))
    context = {'query': query, 'posts': posts}
    return render(request, 'twitter_app/search_results.html')

def post_detail(request, slug):
    post = Post.objects.get(slug__exact = slug)
    post.views += 1
    post.save()
    return render(request, 'twitter_app/post_detail.html', {'post':post})

def sort(request):
    query = request.GET.get('sort')
    posts = Post.objects.order_by(query)
    return render(request, 'twitter_app/sort.html', {'query':query, 'posts':posts})

def save_bg(request):
    if request.method == 'POST':
        form = UserBG('request.POST, request.FILES')
        if form.is_valid():
            form.save(request.user)
        return redirect('index')

def user_detail(request):
    user = User.objects.get(username=username)
    views = user.views_set.order_by('-date')
    comments = user.comment_set.order_by('-date')
    formBG = UserBG()
    context = {'views':views, 'comments':comments, 'formBG':formBG}
    return render(request, 'twitter_app/profile.html', context)

def comment(request, slug):
    post = Post.objects.get(slug__exact = slug)
    if request.method == 'POST':
        post.comment_set.create(user = request.user, text = request.POST.get('text'))
        return redirect(reverse('post_detail_url', kwargs = {'slug':post.slug}))
    return redirect(reverse('post_detial_url', kwargs = {'slug':post.slug}))

def profile(request):
    if not request.user.is_auhenticated:
        return redirect('index')
    views = request.user.views_set.order_by('-date')
    comments = request.user.comment_set.order_by('-date')
    formBG = UserBG()
    context = {'views':views, 'comments':comments, 'formBG':formBG}

def authorisation(request):
    return render(request, 'twitter_app/authorisation.html')