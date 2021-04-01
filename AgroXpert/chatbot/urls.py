from django.urls import path,include
from  chatbot.views import *

urlpatterns=[
path('',Chatbots),#default
path('chatbot',Chatbots)#path('action',function_name),#function will be defined in views action will be performed in the form submitted in html file
]
