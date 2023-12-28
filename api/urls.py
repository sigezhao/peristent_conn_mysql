from django.urls import path
from .views import *

urlpatterns = [
    path('ret/', get_riddle_count, name='get_riddle_count'),
]