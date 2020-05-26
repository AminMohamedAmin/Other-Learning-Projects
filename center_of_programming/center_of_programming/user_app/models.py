from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=150)
    def __str__(self):
        return self.department_name


class Course(models.Model):
    course_dep = models.CharField(max_length=150)
    course_name = models.CharField(max_length=150)
    course_price = models.IntegerField(default=100)
    def __str__(self):
        return self.course_name


class Project(models.Model):
    project_dep = models.CharField(max_length=150)
    project_name = models.CharField(max_length=150)
    project_price = models.IntegerField(default=100)
    def __str__(self):
        return self.project_name


class HtmlRegister(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField(default=0)


class CssRegister(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField(default=0)

class JsRegister(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField(default=0)

class JqRegister(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField(default=0)

class BootstrapRegister(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField(default=0)


class programmers(models.Model):
    prog_dep = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField(default=0)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    address3 = models.CharField(max_length=150)
    address4 = models.CharField(max_length=150)
    #front_id_card = models.ImageField()
    #back_id_card = models.ImageField()