from django.db import models



class Hero(models.Model):
    Title = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Description = models.TextField()


    def __str__(self):
        return self.name

class MyImages(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.url
class Skills(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField()

    def __str__(self):
        return self.name
class ShowCase(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    
class About(models.Model):
    images = models.ManyToManyField(MyImages)
    skills = models.ManyToManyField(Skills)
    title = models.CharField(max_length=100)
    description = models.TextField()
    showCase = models.ManyToManyField(ShowCase)
    cv = models.FileField(upload_to='cv')
    def __str__(self):
        return self.title
    

class ProjectStack(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    stack = models.ManyToManyField(ProjectStack)
    viewProject = models.URLField()
    def __str__(self):
        return self.title
    
class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()
    def __str__(self):
        return self.title


class MyContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name

class ConnectMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name
