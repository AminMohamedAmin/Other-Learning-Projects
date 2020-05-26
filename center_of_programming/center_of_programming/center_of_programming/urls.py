"""center_of_programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_app.views import userhome

# #create api first way
# from user_app import views
#
# #create api second way
# from rest_framework import routers
# r=routers.DefaultRouter()
# r.register('show1',views.register_list2)  #register مش الجدول بتاعنا .. دا فانكشن محجوزة
# rr=routers.DefaultRouter()
# rr.register('show2',views.course_list2)

urlpatterns = [
    path('admin/', admin.site.urls, name= 'admin'),
    path('',userhome,name='userhome'),
    path('user_app/',include('user_app.urls')),
    path('superadmin/', include('superadmin.urls'))

    # #create api first way
    # path('jsonstudent1/', views.register_list1.as_view()),  #register_list اسم الكلاس اللي عملناه في الفيو  #as_view محجوزة.. بتعرض الداتا علي شكل ابااااي
    #
    # #create api second way
    # path('jsonstudent2/', include(r.urls)),
    # path('jsoncourse2/', include(rr.urls))

]
