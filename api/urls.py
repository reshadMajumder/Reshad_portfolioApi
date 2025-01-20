
from django.urls import path
from .views import *

urlpatterns = [
    path('hero/',Hero),
    path('about/', About),
    path('projects/', Projects),
    path('courses/', Courses),
    path('mycontact/', MyContact),
    path('connectme/', ConnectMe),

]
