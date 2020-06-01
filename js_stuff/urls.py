from django.urls import path

from . import views


app_name = 'js_stuff'
urlpatterns = [
    path('', views.index, name='index'),
    path('blur', views.blur, name='blur'),
    path('battleships', views.battleships, name='battleships'),
]
