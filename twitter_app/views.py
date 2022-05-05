from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .models import Post, Favourite, Category
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


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
    return render(request, 'twitter_app/profile.html')

def authorisation(request):
    return render(request, 'twitter_app/authorisation.html')

def favourites(request):
    if request.user.is_authenticated:
        post = Favourite.objects.filter(user=request.user)
        return render(request, 'twitter_app/favourites.html', {'post':post})
    return redirect('authorisation')

def add_to_favourites(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.user.is_authenticated:
        if not request.user.favourite_set.filter(post = post).exists():
            item = Favourite()
            item.post = post
            item.user = request.user
            item.save()
        return redirect('index')
    return redirect('authorisation')

def delete_favourites(request, item_id):
    item = Favourite.objects.get(id=item_id)
    if request.user.is_authenticated:
        item.delete()
        return redirect('favourites')
    return redirect('authorisation')

def create_post(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.category = Category.objects.get(id=request.POST.get('category'))
        post.text = request.POST.get('text')
        if request.FILES.get('image', False) != False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            post.image = filename
        post.save()
    return redirect('index')

def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.category = Category.objects.get(id=request.POST.get('category'))
        if request.FILES.get('image', False) != False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            post.image = filename
        post.save()
        return redirect('index')
    return render(request, 'twitter_app/update.html', {'post':post})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        try:
            post.delete()
            return redirect(reverse('index'))
        except ProtectedError:
            return HttpResponse('Не получилось удалить пост')
    return render(request, 'twitter_app/delete.html', {'post':post})

def messages(request):
    return render(request, 'twitter_app/messages.html')

def edit_profile(request):
    return render(request, 'twitter_app/edit_profile.html')
