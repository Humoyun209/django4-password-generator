from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('showPass/', show_password, name='showPass')
]