
from django.urls import path
from apps.views import HelloTemplateView, Hello2View, ProductJsonUpdateView, \
       HomeTemplateView, ArticleTemplateView, ProductListView, index1_template_view, index2_template_view, \
       post_list_view, post_detail_view, product_form_view, TodoView, TodoDeleteView, register_view, login_view, \
       logout_view, TodoListView, TodoDetailView, UserListView

urlpatterns = [
       path('' , UserListView.as_view()),
       path('hello' ,HelloTemplateView.as_view() ),
       path('hello/path/param/<str:name>' , Hello2View.as_view()),
       path('todos', TodoView.as_view()),
       path('todos/<int:pk>', TodoDetailView.as_view()),
       path('product/update/<int:pk>', ProductJsonUpdateView.as_view()),
       path('home', HomeTemplateView.as_view()),
       path('maqola', ArticleTemplateView.as_view()),

       path('product/list', ProductListView.as_view()),
       path('index1', index1_template_view , name="index1-page"),
       path('index2/<int:num>', index2_template_view , name="index2-page"),
       path('post/list', post_list_view , name="post-list"),
       path('post/detail/<int:pk>', post_detail_view , name="post-detail"),
       path('product/form' , product_form_view , name = 'product-form'),
       path('product/create' , product_form_view , name = 'product-create'),
       path('todo/list' , TodoListView.as_view() , name = 'todo-list'),
       path('todo/delete/<int:pk>' , TodoDeleteView.as_view() , name = 'todo-delete'),
       path('auth/register' , register_view , name = 'register'),
       path('auth/login' , login_view , name = 'login'),
       path('auth/logout' , logout_view , name = 'logout')
]