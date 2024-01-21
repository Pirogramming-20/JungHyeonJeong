from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('like/', like, name='like'),
    path('create_comment/', create_comment, name='create_comment'),
    path('delete_comment/', delete_comment, name='delete_comment'),
]