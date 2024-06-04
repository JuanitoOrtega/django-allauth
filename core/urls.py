from django.urls import path
from core.views import *


urlpatterns = [
    path('', home_view, name='home'),
]
