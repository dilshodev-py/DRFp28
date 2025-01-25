from os.path import join
from sqlite3.dbapi2 import paramstyle

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
import json
from root.settings import BASE_DIR




urlpatterns = [
       path('admin/', admin.site.urls),
       path('' , include('apps.urls'))

]
# http://localhost:8000/todos
# http://localhost:8000/hello?name=Botir
# query param

# http://localhost:8000/Botir
# path param

# http://localhost:8000/hello


