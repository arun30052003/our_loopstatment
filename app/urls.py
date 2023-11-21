from app.views import *
from django.urls import path
app_name='loop'
urlpatterns=[
    path('loop/',loop,name='loop'),
]