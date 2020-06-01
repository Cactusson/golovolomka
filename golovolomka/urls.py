from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('js_stuff.urls')),
    path('admin/', admin.site.urls),
]
