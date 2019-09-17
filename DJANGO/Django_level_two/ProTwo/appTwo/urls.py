from django.urls import path
from appTwo import views

urlpatterns=[
    path('',view.users,name='users')
]
