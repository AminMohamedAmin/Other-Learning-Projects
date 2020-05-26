from django.contrib import admin
from user_app.models import Department, Course, Project

# Register your models here.

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Project)
