from . import views
from django.urls import path

urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),

]
