from django.contrib import admin
from django.urls import path
from main.views import index, create, list, detail
from main.views import index, about, create, list, detail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create),
    path('about/', about),
    path('list/', list),
    path('list/<int:pk>/', detail),
    path('', index),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)