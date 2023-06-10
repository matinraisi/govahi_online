from django.urls import path
from . import views

# app_name = 'login_page'

urlpatterns = [
    path('login/',views.login_page,name='login_page'),
    path('singup/',views.singup_page,name='singup_page'),

]