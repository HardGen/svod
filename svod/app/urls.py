

from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('main/', main, name='main'),
    path('otds/', get_otds, name='otds'),
    path('otd_details/<int:idotd>/', otd_details, name="otd_details"),
    path('food_svod/', food_svod, name="food_svod"),
    path('food_svod/new_svod/', create_new_food_svod),
    path('food_svod/<int:year>/<int:month>/<int:day>/', get_svod_by_date, name='svod_by_date'),
    path('food_svod/update/', update_value),
    path('food_svod/report/<str:datetm>/', report)
]

