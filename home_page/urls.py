from django.urls import path
from . import views

app_name = 'home_page'

urlpatterns = [
    path('',views.home_page,name='home_page'),
    # path('search/',views.search, name='search'),

]