import json
from os.path import join

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.gis.geos.mutable_list import ListMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from apps.models import Product, Post, Todo
from root.settings import BASE_DIR


def hello_view(request):
    name = request.GET.get('name')
    return JsonResponse({"message": f"Hello {name}"})


def hello2_view(request, name):
    return JsonResponse({"message": f"Hello {name}"})


# def todo_list_view(request):
#     with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
#         data = json.load(f)
#     return JsonResponse(data)


def todo_detail_view(request, pk):
    with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
        data = json.load(f)

    for todo in data.get('todos'):
        if todo.get('id') == pk:
            return JsonResponse(todo)
    return JsonResponse({"message": "Not found todo"})


def user_list_view(request):
    users = User.objects.all()

    context = {"users" : users}
    return render(request , 'lesson_2/user-list.html', context)


def product_update_view(request , pk):
    kwargs: dict = {key: value for key , value in request.GET.items()}
    with open(join(BASE_DIR , 'dummy' , 'products.json')) as f:
        products :list[dict]= json.load(f)
        for product in products:
            if product.get('id') == pk:
                product.update(kwargs)
                break
        else:
            return JsonResponse({"message": "Not Found product"} )

    with open(join(BASE_DIR , 'dummy' , 'products.json') , "w") as f:
        json.dump(products , f , indent=3)
    return JsonResponse({"message": "Success edit !"})


def home_view(request):
    return render(request , 'lesson_2/home.html')

def maqola_view(request):
    return render(request , 'lesson_2/maqolalar.html')

def product_list_view(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request , 'lesson_2/product-list.html', context)


def index1_template_view(request):
    return render(request , 'lesson_3/index1.html')

def index2_template_view(request , num):
    return render(request , 'lesson_3/index2.html')

def post_detail_view(request , pk):
    post  = Post.objects.filter(pk = pk).first()
    return render(request , 'lesson_3/post-detail.html' , {'post': post})

def post_list_view(request):
    posts = Post.objects.all()
    return render(request , 'lesson_3/post-list.html' , {"posts" : posts})

def product_form_view(request):
    if request.method == "GET":
        return render(request , 'lesson_4/product-form.html')
    if request.method == "POST":
        post = request.POST
        name = post.get('name')
        price = post.get('price')
        image = request.FILES.get('image')
        Product.objects.create(name=name , price=price , image=image)
        return redirect('product-form')

# request -> url -> view -> response [html , json]



def todo_list_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        todos = Todo.objects.filter(user=request.user)
        context = {'todos' : todos}
        return render(request , 'lesson_4/todo.html' , context)
    if request.method == "POST":
        name = request.POST.get('name')
        Todo.objects.create(name=name , user=request.user)
        return redirect('todo-list')
def todo_delete_view(request , pk):
    Todo.objects.filter(pk = pk).delete()
    return redirect('todo-list')

def register_view(request):
    if request.method == "GET":
        return render(request , 'auth/register.html')
    if request.method == "POST":
        data = dict(request.POST.items())
        del data['csrfmiddlewaretoken']
        data['password'] = make_password(data.get('password'))
        user = User.objects.filter(username=data.get('username'))
        if not user.exists():
            User.objects.create(**data)
        return render(request , 'auth/register.html')

def login_view(request):
    if request.method == "GET":
        return render(request , 'auth/login.html')
    if request.method == 'POST':
        post=  request.POST
        username = post.get('username')
        password = post.get('password') # un hash
        user = User.objects.filter(username = username)
        if user.exists():
            user = user.first()
            if check_password(password , user.password):
                login(request , user)
                context = {'todos' : Todo.objects.filter(user=request.user)}
                return render(request , 'lesson_4/todo.html' ,context )
            else:
                messages.error(request , 'Password not match')
        messages.error(request , 'User not found')
        return redirect('login')


def logout_view(request):
    logout(request)
    return render(request , 'auth/login.html')


# View
# CreateView
# UpdateView
# DeleteView
# ListView

