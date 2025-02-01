from os.path import join
from sqlite3.dbapi2 import paramstyle

from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
import json
from root.settings import  MEDIA_URL, MEDIA_ROOT

urlpatterns = [
       path('admin/', admin.site.urls),
       path('' , include('apps.urls'))

] + static(MEDIA_URL , document_root = MEDIA_ROOT)
# http://localhost:8000/todos
# http://localhost:8000/hello?name=Botir
# query param

# http://localhost:8000/Botir
# path param

# http://localhost:8000/hello


