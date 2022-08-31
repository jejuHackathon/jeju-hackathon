from django.contrib import admin
from django.urls import path
from main.views import index, create, list, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create),
    path('list/', list),
    path('detail/', detail),
    path('', index),
]