from django.contrib import admin
from django.urls import path
from main.views import index, about, create, home, list, detail, update, delete
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('delete/<int:pk>/', delete),
    path('update/<int:pk>/', update),
    path('create/', create),
    path('list/', list),
    path('list/<int:pk>/', detail),
    path('home/', home),
    path('', index),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)