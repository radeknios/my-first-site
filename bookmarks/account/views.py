"""from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
				password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakonczyło się sukcesem.')
                else:
	                return HttpResponse('Konto jest zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, AddPostForm, AddAvailable
from .models import Profile, Post, Category, SubCategory
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime, timedelta
#from django.template import RequestContext

@login_required
def dashboard(request):
    days = 30
    posts = Post.objects.filter(publish__gte = timezone.now() - timedelta(days=days))
    #posts = Post.objects.all()
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'posts': posts})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile, 
                                    data=request.POST, 
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form' : profile_form})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'account/detail.html', {'post': post})

@login_required
def new_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish = timezone.now()
            post.save()
    else:
        form = AddPostForm()
    return render(request, 'account/new_post.html', {'form': form})
@login_required
def your_posts(request):
    posts = Post.objects.filter(author = request.user)
    return render(request, 'account/your_posts.html', {'posts': posts})

@login_required
def delete_post(request, id):
    del_post = get_object_or_404(Post, id=id, author=request.user)
    del_post.delete()
    return render(request, 'account/delete_post.html', {'del_post': del_post})
   
@login_required
def add_available(request):
    if request.method == "POST":
        form = AddAvailable(request.POST)
        if form.is_valid():
            available = form.save(commit=False)
            available.user = request.user
            available.save()
    else:
        form = AddAvailable()
    return render(request, 'account/available_add.html', {'form': form})

def show_genres(request):
    categories = Category.objects.all()
    #subcategories = SubCategory.objects.filter(category = categories)
    return render(request, "account/genres.html", {'categories': categories}, '''{'subcategories' : subcategories}''')

def list_of_post_by_category(request, slug):
    #categories = Category.objects.all()
    #days = 30
    #post = Post.objects.filter(publish__gte = timezone.now() - timedelta(days=days))
    #post = Post.objects.all()
    #if category_slug:
    category=get_object_or_404(Category, slug = slug)
    posts = Post.objects.filter(category=category)
    return render(request, "account/list_of_post_by_category.html", {'posts': posts, 'category': category})
    
    
