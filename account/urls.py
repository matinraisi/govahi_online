from django.urls import path
from . import views

app_name = 'login_page'

urlpatterns = [
    path('',views.login_page,name='login_page'),
]