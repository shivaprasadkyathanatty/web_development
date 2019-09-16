from django.urls import path
from two_app import views

urlpatterns=[
    path('',views.index,name='index')
]
