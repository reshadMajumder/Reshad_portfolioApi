from django.db import models



class Hero(models.Model):
    Title = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Description = models.TextField()
    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Hero'


    def __str__(self):
        return self.name

class MyImages(models.Model):
    image = models.ImageField(upload_to='images')
    class Meta:
        verbose_name = 'MyImages'
        verbose_name_plural = 'MyImages'

    def __str__(self):
        return self.image.url
class Skills(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField()
    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'


    def __str__(self):
        return self.name
class ShowCase(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        verbose_name = 'ShowCase'
        verbose_name_plural = 'ShowCase'

    def __str__(self):
        return self.title
    
class About(models.Model):
    images = models.ManyToManyField(MyImages)
    skills = models.ManyToManyField(Skills)
    title = models.CharField(max_length=100)
    description = models.TextField()
    showCase = models.ManyToManyField(ShowCase)
    cv = models.FileField(upload_to='cv')
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title
    

class ProjectStack(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'ProjectStack'
        verbose_name_plural = 'ProjectStack'

    def __str__(self):
        return self.name
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    stack = models.ManyToManyField(ProjectStack)
    viewProject = models.URLField()
    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
    
class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()
    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class MyContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    class Meta:
        verbose_name = 'MyContact'
        verbose_name_plural = 'MyContact'

    def __str__(self):
        return self.name

class ConnectMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    class Meta:
        verbose_name = 'ConnectMe'
        verbose_name_plural = 'ConnectMe'

    def __str__(self):
        return self.name
