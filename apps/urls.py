
from django.urls import path

from apps.views import hello_view, hello2_view, todo_list_view, todo_detail_view, index_view

urlpatterns = [
       path('' , index_view),

       path('hello' ,hello_view ),
       path('hello/path/param/<str:name>' , hello2_view),
       path('todos', todo_list_view),
       path('todos/<int:pk>', todo_detail_view),

]