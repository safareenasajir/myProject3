from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo1,name='demo1'),
    path('',views.demo,name='demo'),
    #path('add/',views.addition,name="addition")
]

