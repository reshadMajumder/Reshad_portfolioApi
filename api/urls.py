from django.urls import path
from . import views

urlpatterns = [
    path('hero/', views.hero_view, name='hero'),
    path('about/', views.about_view, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('courses/', views.courses_view, name='courses'),
    path('my-contact/', views.my_contact_view, name='my-contact'),
    path('connect-me/', views.connect_me_view, name='connect-me'),
]
