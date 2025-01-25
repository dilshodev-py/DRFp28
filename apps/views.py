import json
from os.path import join
from typing import reveal_type

from django.http import JsonResponse
from django.shortcuts import render, redirect

from root.settings import BASE_DIR


# Create your views here.
def hello_view(request):
    name = request.GET.get('name')
    return JsonResponse({"message": f"Hello {name}"})


def hello2_view(request, name):
    return JsonResponse({"message": f"Hello {name}"})


def todo_list_view(request):
    with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
        data = json.load(f)
    return JsonResponse(data)


def todo_detail_view(request, pk):
    with open(join(BASE_DIR, 'dummy', 'todos.json')) as f:
        data = json.load(f)

    for todo in data.get('todos'):
        if todo.get('id') == pk:
            return JsonResponse(todo)
    return JsonResponse({"message": "Not found todo"})


def index_view(request):
    name = request.GET.get("name")
    num = request.GET.get("num")
    range_numbers = list(range(0,int(num),2))
    return render(request , 'index.html' , context={"name" : name , "nums" : range_numbers})
