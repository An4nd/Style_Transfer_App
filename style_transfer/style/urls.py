
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='homepage'),
    path('stylee',views.stylee,name='stylee'),
    path('about',views.about,name='about'),
    ]