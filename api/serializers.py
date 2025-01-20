from rest_framework import serializers
from .models import *

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class MyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyImages
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class ShowCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowCase
        fields = '__all__'



class AboutSerializer(serializers.ModelSerializer):
    images = MyImagesSerializer(many=True)
    skills = SkillsSerializer(many=True)
    showCase = ShowCaseSerializer(many=True)
    class Meta:
        model = About
        fields = '__all__'




class ProjectStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStack
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    stack = ProjectStackSerializer(many=True)
    class Meta:
        model = Projects
        fields = '__all__'



class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'  

class MyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyContact
        fields = '__all__'

class ConnectMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectMe
        fields = '__all__'
