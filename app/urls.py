from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('try-free-lesson', views.try_free_lesson),
    path('connect', views.connect),


]
