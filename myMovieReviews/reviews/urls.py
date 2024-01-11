from django.urls import path, include
from .views import *

urlpatterns = [
    path('', reviews_list),
    path('<int:pk>', reviews_detail),
    path('create', reviews_create),
]