import json
import random
from datetime import timedelta
from os.path import join

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import prefetch_related_objects, F
from django.db.models.fields import return_None
from django.db.models.functions import Upper
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, View, ListView, DeleteView, FormView, UpdateView

from apps.forms import TodoModelForm, ProductModelForm, ProductForm, RegisterModelForm, VerifyForm, redis
from apps.models import Product, Post, Todo, Category, User
from apps.tasks import send_mail
from root.settings import BASE_DIR, EMAIL_HOST, EMAIL_HOST_USER


# generic.View
# generic.ListView
# generic.TemplateView

# generic.DeleteView
# generic.UpdateView
# generic.CreateView
# generic.FormView
# generic.DetailView
# generic.TodayArchiveView
# generic.MonthArchiveView
# generic.YearArchiveView
# generic.WeekArchiveView
# generic.RedirectView





# def hello_view(request):
#     name = request.GET.get('name')
#     return JsonResponse({"message": f"Hello {name}"})

class HelloTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data : dict = super().get_context_data(**kwargs)
        data["name"] = self.request.GET.get('name')
        data["nums"] = list(range(int(self.request.GET.get('num'))))
        return data


# def hello2_view(request, name):
#     return JsonResponse({"message": f"Hello {name}"})

class Hello2View(View):
    def get(self , request , name ):
        return JsonResponse({"message" : f"Hello {name}"})



# def todo_list_view(request):
#     with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
#         data = json.load(f)
#     return JsonResponse(data)
#
class TodoView(View):
    def get(self , request ):
        with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
            data = json.load(f)
        return JsonResponse(data)


# def todo_detail_view(request, pk):
#     with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
#         data = json.load(f)
#
#     for todo in data.get('todos'):
#         if todo.get('id') == pk:
#             return JsonResponse(todo)
#     return JsonResponse({"message": "Not found todo"})

class TodoDetailView(View):
    def get(self , request, pk ):
        with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
            data = json.load(f)
        for todo in data.get('todos'):
            if todo.get('id') == pk:
                return JsonResponse(todo)
        return JsonResponse({"message": "Not found todo"})

# def user_list_view(request):
#     users = User.objects.all()
#
#     context = {"users" : users}
#     return render(request , 'lesson_2/user-list.html', context)

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'lesson_2/user-list.html'
    context_object_name = "users"



# def product_update_view(request , pk):
#     kwargs: dict = {key: value for key , value in request.GET.items()}
#     with open(join(BASE_DIR , 'dummy' , 'products.json')) as f:
#         products :list[dict]= json.load(f)
#         for product in products:
#             if product.get('id') == pk:
#                 product.update(kwargs)
#                 break
#         else:
#             return JsonResponse({"message": "Not Found product"} )
#
#     with open(join(BASE_DIR , 'dummy' , 'products.json') , "w") as f:
#         json.dump(products , f , indent=3)
#     return JsonResponse({"message": "Success edit !"})

class ProductJsonUpdateView(View):
    def get(self , request , pk):
        kwargs: dict = {key: value for key, value in request.GET.items()}
        with open(join(BASE_DIR, 'dummy', 'products.json')) as f:
            products: list[dict] = json.load(f)
            for product in products:
                if product.get('id') == pk:
                    product.update(kwargs)
                    break
            else:
                return JsonResponse({"message": "Not Found product"})

        with open(join(BASE_DIR, 'dummy', 'products.json'), "w") as f:
            json.dump(products, f, indent=3)
        return JsonResponse({"message": "Success edit !"})

# def home_view(request):
#     return render(request , 'lesson_2/home.html')


class HomeTemplateView(TemplateView):
    template_name = 'lesson_2/home.html'


# def maqola_view(request):
#     return render(request , 'lesson_2/maqolalar.html')
class ArticleTemplateView(TemplateView):
    template_name = 'lesson_2/maqolalar.html'

# def product_list_view(request):
#     products = Product.objects.all()
#     users = User.objects.all()
#     context = {"products" : products , "users" : users}
#     return render(request , 'lesson_2/product-list.html', context)

# class ProductListView(ListView):
#     queryset = Product.objects.all()
#     template_name = 'lesson_2/product-list.html'
#     context_object_name = 'products'
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['users'] = User.objects.all()
#         return data


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

# def todo_list_view(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#
#     if request.method == 'GET':
#         todos = Todo.objects.filter(user=request.user)
#         context = {'todos' : todos}
#         return render(request , 'lesson_4/todo.html' , context)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         Todo.objects.create(name=name , user=request.user)
#         return redirect('todo-list')

class TodoListView(LoginRequiredMixin,ListView , FormView):
    queryset = Todo.objects.all()
    template_name = 'lesson_4/todo.html'
    login_url = reverse_lazy('login')
    context_object_name = 'todos'
    success_url = reverse_lazy('todo-list')
    form_class = TodoModelForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super().form_valid(form)



# def todo_delete_view(request , pk):
#     Todo.objects.filter(pk = pk).delete()
#     return redirect('todo-list')

class TodoDeleteView(DeleteView):
    queryset = Todo.objects.all()
    template_name = 'lesson_4/todo.html'
    success_url = reverse_lazy('todo-list')
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['todos'] = Todo.objects.all()
        return data



# def register_view(request):
#     if request.method == "GET":
#         return render(request , 'auth/register.html')
#     if request.method == "POST":
#         data = dict(request.POST.items())
#         del data['csrfmiddlewaretoken']
#         data['password'] = make_password(data.get('password'))
#         user = User.objects.filter(username=data.get('username'))
#         if not user.exists():
#             User.objects.create(**data)
#         return render(request , 'auth/register.html')

class RegisterFormView(FormView):
    form_class = RegisterModelForm
    template_name = 'lesson_7/register-form.html'
    success_url = reverse_lazy('verify')

    def form_valid(self, form):
        email=  form.cleaned_data.get('email')
        form.save()
        r_code = random.randrange(10**5 , 10**6)
        redis.set(email , r_code)
        redis.expire(email , time=timedelta(minutes=2))
        send_mail(email , r_code)
        response =  HttpResponseRedirect(self.get_success_url())
        response.set_cookie('email' , email)
        return response


    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)


class VerifyCodeView(FormView):
    form_class = VerifyForm
    template_name = 'lesson_7/verify.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        code = form.cleaned_data.get('code')
        email = self.request.COOKIES.get('email')
        verify_code = redis.get(email)
        if not verify_code:
            messages.error(self.request, "Codni mudati o'tgan")
            return self.form_invalid(form)
        if str(verify_code) != str(code):
            messages.error(self.request, 'Code not match !')
            return self.form_invalid(form)
        redis.delete(email)
        form.update(email)
        return super().form_valid(form)

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return super().form_invalid(form)


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

# """
#
#
# SELECT username, first_name, last_name, email FROM auth_user
# WHERE first_name LIKE 'R%' OR last_name LIKE 'D%';
#
# select id , name from apps_category
# where name like 'C%' or name like 'D%';
#
# """
# from django.db.models import Q
# queryset = Category.objects.filter(
#         name__startswith='R'
#     ) | Category.objects.filter(
#     name__startswith='D'
# )
#
# qs = Category.objects.filter(Q(name__startswith='R') | Q(name__startswith="C"))
#
# print(qs.query)

# select_related
# prefetch_related

# Product.objects.filter()
# Category.objects.all().values('name' , 'products__name')
# Product.objects.all().values('name' , 'category__name')


# Product.objects.all().values('category' , 'name')


# Category.objects.filter(pk=1).delete()
# Category.objects.filter(pk=1).update(name='C12')

# Category.objects.all().prefetch_related('products')
# Product.objects.all().select_related('category')
#
#
# Category.objects.bulk_create([
#     Category(name='C6'),
#     Category(name='C7'),
#     Category(name='C8'),
#     Category(name='C9'),
#     Category(name='C610'),
#     Category(name='C11'),
#     Category(name='C11'),
# ])

# Category.objects.all()[0]
# Category.objects.all().first()

# Category.objects.all().filter(pk=1)
# Category.objects.filter(pk=1)
# Category.objects.get(pk=1)
# Category.objects.filter(pk=1)
#
# obj , is_create = Category.objects.get_or_create(name='C13')
# Category.objects.count()


# Category.objects.filter(pk=20).exists()
# bool(Category.objects.filter(pk=20))

# await Category.objects.abulk_create()
# Category.objects.bulk_create()

# obj , is_update = Category.objects.update_or_create(pk=1,defaults={"name":"C20"})


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'lesson_5/product-list.html'
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    success_url = reverse_lazy('product-list')
    form_class = ProductModelForm
    pk_url_kwarg = 'pk'

class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    success_url = reverse_lazy('product-list')
    pk_url_kwarg = 'pk'


class ProductFormView(FormView):
    form_class = ProductModelForm
    template_name = 'lesson_7/form-product.html'
    success_url = reverse_lazy('product-form')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        message = "\n".join([i[0] for i in form.errors.values()])
        messages.error(self.request , message)
        return super().form_invalid(form)


