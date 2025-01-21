from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['GET','POST','PUT','DELETE'])
def hero_view(request):
    if request.method == 'GET':
        hero = Hero.objects.all()
        serializer = HeroSerializer(hero, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        hero = Hero.objects.first()
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        hero = Hero.objects.first()
        hero.delete()
        return Response(status=204)

@api_view(['GET','POST','PUT','DELETE'])
def about_view(request):
    if request.method == 'GET':
        about = About.objects.first()
        serializer = AboutSerializer(about)  # Removed many=True since we're getting one object
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        about = About.objects.first()
        serializer = AboutSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        about = About.objects.first()
        about.delete()
        return Response(status=204)
    
@api_view(['GET','POST','PUT','DELETE'])
def projects_view(request):
    if request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  
    elif request.method == 'PUT':
        project = Projects.objects.get(id=request.data.get('id'))
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        project = Projects.objects.get(id=request.data.get('id'))
        project.delete()
        return Response(status=204) 

@api_view(['GET','POST','PUT','DELETE'])
def courses_view(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  
    elif request.method == 'PUT':
        course = Courses.objects.get(id=request.data.get('id'))
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        course = Courses.objects.get(id=request.data.get('id'))
        course.delete()
        return Response(status=204)     

@api_view(['GET','POST','PUT','DELETE'])
def my_contact_view(request):
    if request.method == 'GET':
        my_contact = MyContact.objects.all()
        serializer = MyContactSerializer(my_contact, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MyContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  
    elif request.method == 'PUT':
        contact = MyContact.objects.get(id=request.data.get('id'))
        serializer = MyContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        contact = MyContact.objects.get(id=request.data.get('id'))
        contact.delete()
        return Response(status=204) 

@api_view(['GET','POST','PUT','DELETE'])
def connect_me_view(request):
    if request.method == 'GET':
        connect_me = ConnectMe.objects.all()
        serializer = ConnectMeSerializer(connect_me, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ConnectMeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        connect = ConnectMe.objects.get(id=request.data.get('id'))
        serializer = ConnectMeSerializer(connect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        connect = ConnectMe.objects.get(id=request.data.get('id'))
        connect.delete()
        return Response(status=204)






