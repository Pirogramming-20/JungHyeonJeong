from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
    path('', devtools_list, name='list'),
    path('create/', create, name='create'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('search/', search, name='search'),
]