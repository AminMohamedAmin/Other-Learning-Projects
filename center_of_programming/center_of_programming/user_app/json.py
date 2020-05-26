#create api
from .models import Register, Course
from rest_framework import serializers
class jsonregister(serializers.ModelSerializer):
    class Meta:           #Meta محجوزة وثابتة
        model=Register    #model محجوزة وثابتة  #Register اسم الجدول
        fields='__all__'  #fields محجوزة وثابتة #fields={'id', 'name'} لو مش عايز كل الاعمدة من الجدول


class jsoncourse(serializers.ModelSerializer):
    class Meta:           #Meta محجوزة وثابتة
        model=Course    #model محجوزة وثابتة  #Register اسم الجدول
        fields='__all__'  #fields محجوزة وثابتة #fields={'id', 'name'} لو مش عايز كل الاعمدة من الجدول
