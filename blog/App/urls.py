from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('detail/<int:pk>/',views.Detail,name='detail'),
    path('about/',views.About,name='about')
]


