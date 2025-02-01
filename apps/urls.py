
from django.urls import path

from apps.views import hello_view, hello2_view, todo_detail_view, product_update_view, \
       home_view, maqola_view, user_list_view, product_list_view, index1_template_view, index2_template_view, \
       post_list_view, post_detail_view, product_form_view, todo_list_view, todo_delete_view, register_view, login_view,logout_view

urlpatterns = [
       path('' , user_list_view),
       path('hello' ,hello_view ),
       path('hello/path/param/<str:name>' , hello2_view),
       path('todos', todo_list_view),
       path('todos/<int:pk>', todo_detail_view),
       path('product/update/<int:pk>', product_update_view),
       path('home', home_view),
       path('maqola', maqola_view),

       path('product/list', product_list_view),
       path('index1', index1_template_view , name="index1-page"),
       path('index2/<int:num>', index2_template_view , name="index2-page"),
       path('post/list', post_list_view , name="post-list"),
       path('post/detail/<int:pk>', post_detail_view , name="post-detail"),
       path('product/form' , product_form_view , name = 'product-form'),
       path('product/create' , product_form_view , name = 'product-create'),
       path('todo/list' , todo_list_view , name = 'todo-list'),
       path('todo/delete/<int:pk>' , todo_delete_view , name = 'todo-delete'),
       path('auth/register' , register_view , name = 'register'),
       path('auth/login' , login_view , name = 'login'),
       path('auth/logout' , logout_view , name = 'logout')
]