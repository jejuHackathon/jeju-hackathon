from django.contrib import admin
from django.urls import path
from main.views import index, home, about, create, list, detail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', home),
    path('about/', about),
    path('create/', create),
    path('list/', list),
    path('list/<int:pk>/', detail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)