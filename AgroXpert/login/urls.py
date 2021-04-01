from django.urls import path,include
from login.views import *

urlpatterns=[
    path('',home,name='home'),
    path('admin',admin,name='admin'),
    path('adminLogin',admin,name='admin'),
    path('farmerLogin',farmer,name='admin'),
    path('signin',signin,name='signin'),
    path('signup',signup,name='signup'),

]