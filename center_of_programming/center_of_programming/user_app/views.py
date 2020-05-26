from django.shortcuts import render
from user_app import models

# #create api first way
# from .json import jsonregister, jsoncourse
# from rest_framework.views import APIView
# from .models import Register, Course
# from rest_framework.response import Response
# #يوجد امبورت هنا تخص ايضا الطريقة الثانية والعكس
#
# #create api second way
# from rest_framework import viewsets

# Create your views here.


def userhome(request):
    return render(request, 'userhome.html', {})


def frontend(request):
    return render(request, 'frontend/frontend.html', {})


def backend(request):
    return render(request, 'backend.html', {})


def android(request):
    return render(request, 'android.html', {})


def fullstack(request):
    return render(request, 'fullstack.html', {})

############### Html Front End ###################
def htmlregister(request):
    course = models.Course.objects.filter(course_name='HTML / HTML 5')
    department=models.Department.objects.filter(department_name='Front End')
    if department.exists():
        if course.exists():
            return render(request, 'frontend/necessarycourses/html/htmlregister.html', {})
        else:
            msg='course is not available now'
            return render(request, 'frontend/frontend.html', {'htmlmsg':msg})
    else:
        msg = 'department is not available now'
        return render(request, 'frontend/frontend.html', {'htmlmsg': msg})

def htmlsaveregister(request):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.HtmlRegister()
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1=new.id
    data2=new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='HTML / HTML 5')
    newd = models.Department.objects.get(department_name='Front End')
    data3=newc.course_name
    data4=newd.department_name
    data5=newc.course_price
    return render(request, 'frontend/necessarycourses/html/htmlshow.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})
    #except:
        #msg = 'fill all fields with a correct data'
        #return render(request, 'frontend/necessarycourses/html/htmlregister.html', {'msg': msg})

def htmlupdate(request,id):
    d=models.HtmlRegister.objects.get(id=id)
    data1=d.first_name
    data2=d.second_name
    data3=d.third_name
    data4=d.last_name
    data5=d.email
    data6=d.mobile
    data7=d.id
    return render(request, 'frontend/necessarycourses/html/htmlupdate.html', {'st_id':id, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7})


def htmlsaveupdate(request,id):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.HtmlRegister(id=id)
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1 = new.id
    data2 = new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='HTML / HTML 5')
    newd = models.Department.objects.get(department_name='Front End')
    data3 = newc.course_name
    data4 = newd.department_name
    data5 = newc.course_price
    return render(request, 'frontend/necessarycourses/html/htmlshow.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/html/htmlupdate.html', {'msg': msg})


def htmldelete(request,id):
    old=models.HtmlRegister(id=id)
    old.delete()
    return render(request, 'frontend/frontend.html', {})






############### Css Front End ###################
def cssregister(request):
    course = models.Course.objects.filter(course_name='CSS / CSS3')
    department=models.Department.objects.filter(department_name='Front End')
    if department.exists():
        if course.exists():
            return render(request, 'frontend/necessarycourses/css/cssregister.html', {})
        else:
            msg='course is not available now'
            return render(request, 'frontend/frontend.html', {'cssmsg':msg})
    else:
        msg = 'department is not available now'
        return render(request, 'frontend/frontend.html', {'cssmsg': msg})

def csssaveregister(request):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.CssRegister()
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1=new.id
    data2=new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='CSS / CSS3')
    newd = models.Department.objects.get(department_name='Front End')
    data3=newc.course_name
    data4=newd.department_name
    data5=newc.course_price
    return render(request, 'frontend/necessarycourses/css/cssshow.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/css/cssregister.html', {'msg': msg})

def cssupdate(request,id):
    d=models.CssRegister.objects.get(id=id)
    data1=d.first_name
    data2=d.second_name
    data3=d.third_name
    data4=d.last_name
    data5=d.email
    data6=d.mobile
    data7=d.id
    return render(request, 'frontend/necessarycourses/css/cssupdate.html', {'st_id':id, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7})


def csssaveupdate(request,id):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.CssRegister(id=id)
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1 = new.id
    data2 = new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='CSS / CSS3')
    newd = models.Department.objects.get(department_name='Front End')
    data3 = newc.course_name
    data4 = newd.department_name
    data5 = newc.course_price
    return render(request, 'frontend/necessarycourses/css/cssshow.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/css/cssupdate.html', {'msg': msg})


def cssdelete(request,id):
    old=models.CssRegister(id=id)
    old.delete()
    return render(request, 'frontend/frontend.html', {})









############### Js Front End ###################
def jsregister(request):
    course = models.Course.objects.filter(course_name='JavaScript')
    department=models.Department.objects.filter(department_name='Front End')
    if department.exists():
        if course.exists():
            return render(request, 'frontend/necessarycourses/js/jsregister.html', {})
        else:
            msg='course is not available now'
            return render(request, 'frontend/frontend.html', {'jsmsg':msg})
    else:
        msg = 'department is not available now'
        return render(request, 'frontend/frontend.html', {'jsmsg': msg})

def jssaveregister(request):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.JsRegister()
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1=new.id
    data2=new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='JavaScript')
    newd = models.Department.objects.get(department_name='Front End')
    data3=newc.course_name
    data4=newd.department_name
    data5=newc.course_price
    return render(request, 'frontend/necessarycourses/js/jsshow.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/js/jsregister.html', {'msg': msg})

def jsupdate(request,id):
    d=models.JsRegister.objects.get(id=id)
    data1=d.first_name
    data2=d.second_name
    data3=d.third_name
    data4=d.last_name
    data5=d.email
    data6=d.mobile
    data7=d.id
    return render(request, 'frontend/necessarycourses/js/jsupdate.html', {'st_id':id, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7})


def jssaveupdate(request,id):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.JsRegister(id=id)
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1 = new.id
    data2 = new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='JavaScript')
    newd = models.Department.objects.get(department_name='Front End')
    data3 = newc.course_name
    data4 = newd.department_name
    data5 = newc.course_price
    return render(request, 'frontend/necessarycourses/js/jsshow.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/js/jsupdate.html', {'msg': msg})


def jsdelete(request,id):
    old=models.JsRegister(id=id)
    old.delete()
    return render(request, 'frontend/frontend.html', {})






############### Jq Front End ###################
def jqregister(request):
    course = models.Course.objects.filter(course_name='jQuery')
    department=models.Department.objects.filter(department_name='Front End')
    if department.exists():
        if course.exists():
            return render(request, 'frontend/necessarycourses/jq/jqregister.html', {})
        else:
            msg='course is not available now'
            return render(request, 'frontend/frontend.html', {'jqmsg':msg})
    else:
        msg = 'department is not available now'
        return render(request, 'frontend/frontend.html', {'jqmsg': msg})

def jqsaveregister(request):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.JqRegister()
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1=new.id
    data2=new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='jQuery')
    newd = models.Department.objects.get(department_name='Front End')
    data3=newc.course_name
    data4=newd.department_name
    data5=newc.course_price
    return render(request, 'frontend/necessarycourses/jq/jqshow.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/jq/jqregister.html', {'msg': msg})

def jqupdate(request,id):
    d=models.JqRegister.objects.get(id=id)
    data1=d.first_name
    data2=d.second_name
    data3=d.third_name
    data4=d.last_name
    data5=d.email
    data6=d.mobile
    data7=d.id
    return render(request, 'frontend/necessarycourses/js/templates/frontend/jq/jqupdate.html', {'st_id':id, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7})


def jqsaveupdate(request,id):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.JqRegister(id=id)
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1 = new.id
    data2 = new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='jQuery')
    newd = models.Department.objects.get(department_name='Front End')
    data3 = newc.course_name
    data4 = newd.department_name
    data5 = newc.course_price
    return render(request, 'frontend/necessarycourses/jq/jqshow.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/js/templates/frontend/jq/jqupdate.html', {'msg': msg})


def jqdelete(request,id):
    old=models.JqRegister(id=id)
    old.delete()
    return render(request, 'frontend/frontend.html', {})







############### Bootstrap Front End ###################
def bootregister(request):
    course = models.Course.objects.filter(course_name='Bootstrap')
    department=models.Department.objects.filter(department_name='Front End')
    if department.exists():
        if course.exists():
            return render(request, 'frontend/necessarycourses/bootstrap/bootregister.html', {})
        else:
            msg='course is not available now'
            return render(request, 'frontend/frontend.html', {'bootmsg':msg})
    else:
        msg = 'department is not available now'
        return render(request, 'frontend/frontend.html', {'bootmsg': msg})

def bootsaveregister(request):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.BootstrapRegister()
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1=new.id
    data2=new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='Bootstrap')
    newd = models.Department.objects.get(department_name='Front End')
    data3=newc.course_name
    data4=newd.department_name
    data5=newc.course_price
    return render(request, 'frontend/necessarycourses/bootstrap/bootshow.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/bootstrap/bootregister.html', {'msg': msg})

def bootupdate(request,id):
    d=models.BootstrapRegister.objects.get(id=id)
    data1=d.first_name
    data2=d.second_name
    data3=d.third_name
    data4=d.last_name
    data5=d.email
    data6=d.mobile
    data7=d.id
    return render(request, 'frontend/necessarycourses/bootstrap/bootupdate.html', {'st_id':id, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7})


def bootsaveupdate(request,id):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new = models.BootstrapRegister(id=id)
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.save()
    data1 = new.id
    data2 = new.first_name + " " + new.second_name + " " + new.third_name + " " + new.last_name
    newc = models.Course.objects.get(course_name='Bootstrap')
    newd = models.Department.objects.get(department_name='Front End')
    data3 = newc.course_name
    data4 = newd.department_name
    data5 = newc.course_price
    return render(request, 'frontend/necessarycourses/bootstrap/bootshow.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
    #except:
     #   msg = 'fill all fields with a correct data'
      #  return render(request, 'frontend/necessarycourses/bootstrap/bootupdate.html', {'msg': msg})


def bootdelete(request,id):
    old=models.BootstrapRegister(id=id)
    old.delete()
    return render(request, 'frontend/frontend.html', {})


def allnecessary(request):
    #course = models.Course.objects.filter(course_name='HTML / HTML 5' or 'CSS / CSS3' or 'JavaScript' or 'JQuery' or 'Bootstrap')
    course1 = models.Course.objects.filter(course_name='HTML / HTML 5')
    course2 = models.Course.objects.filter(course_name='CSS / CSS3')
    course3 = models.Course.objects.filter(course_name='JavaScript')
    course4 = models.Course.objects.filter(course_name='JQuery')
    course5 = models.Course.objects.filter(course_name='Bootstrap')

    department=models.Department.objects.filter(department_name='Front End')
    if department.exists():
        #if course.exists():
        if course1.exists()==False and course2.exists()==True and course3.exists()==True and course4.exists()==True and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html course is not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==False and course3.exists()==True and course4.exists()==True and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and CSS courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==True and course3.exists()==False and course4.exists()==True and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and JavaScript course are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==True and course3.exists()==True and course4.exists()==False and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and JQuery courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==True and course3.exists()==True and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and Bootstrap courses are not available now. Other courses are available'})

        elif course1.exists()==False and course2.exists()==False and course3.exists()==False and course4.exists()==True and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and CSS and JavaScript courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==False and course3.exists()==False and course4.exists()==False and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and CSS and JavaScript and JQuery courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==False and course3.exists()==True and course4.exists()==False and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and CSS and JQuery courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==False and course3.exists()==True and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and CSS and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==True and course3.exists()==False and course4.exists()==False and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and JavaScript and JQuery courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==True and course3.exists()==False and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and JavaScript and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==True and course3.exists()==True and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and JQuery and Bootstrap courses are not available now. Other courses are available'})

        elif course1.exists()==True and course2.exists()==False and course3.exists()==False and course4.exists()==True and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'CSS and JavaScript courses are not available now. Other courses are available'})
        elif course1.exists()==True and course2.exists()==False and course3.exists()==True and course4.exists()==False and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'CSS and JQuery courses are not available now. Other courses are available'})
        elif course1.exists()==True and course2.exists()==False and course3.exists()==True and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'CSS and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==True and course2.exists()==False and course3.exists()==False and course4.exists()==False and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'CSS and JavaScript and JQuery courses are not available now. Other courses are available'})
        elif course1.exists()==True and course2.exists()==False and course3.exists()==False and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'CSS and JavaScript and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==True and course2.exists()==False and course3.exists()==True and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'CSS and JQuery and Bootstrap courses are not available now. Other courses are available'})

        elif course1.exists()==True and course2.exists()==False and course3.exists()==False and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'CSS and JavaScript and JQuery and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==True and course3.exists()==False and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and JavaScript and JQuery and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==False and course3.exists()==True and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and CSS and JQuery and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==False and course2.exists()==False and course3.exists()==False and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Html and CSS and JavaScript and Bootstrap courses are not available now. Other courses are available'})


        elif course1.exists()==True and course2.exists()==True and course3.exists()==False and course4.exists()==False and course5.exists()==True:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'JavaScript and JQuery courses are not available now. Other courses are available'})
        elif course1.exists()==True and course2.exists()==True and course3.exists()==False and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'JavaScript and Bootstrap courses are not available now. Other courses are available'})
        elif course1.exists()==True and course2.exists()==True and course3.exists()==False and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'JavaScript and Jquery and Bootstrap courses are not available now. Other courses are available'})

        elif course1.exists()==True and course2.exists()==True and course3.exists()==True and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'JQuery and Bootstrap courses are not available now. Other courses are available'})

        elif course1.exists()==True and course2.exists()==True and course3.exists()==True and course4.exists()==True and course5.exists()==False:
            return render(request, 'frontend/necessarycourses/registerall.html',{'hmsg': 'Bootstrap course is not available now. Other courses are available'})

        elif course1.exists()==False and course2.exists()==False and course3.exists()==False and course4.exists()==False and course5.exists()==False:
            return render(request, 'frontend/frontend.html',{'hmsg': 'necessary courses are not available now'})

        else:
            return render(request, 'frontend/necessarycourses/registerall.html', {})
    else:
        msg = 'department is not available now'
        return render(request, 'frontend/frontend.html', {'allmsg': msg})


def allnecessarysave(request):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    #try:
    new1 = models.HtmlRegister()
    new1.first_name = first_name
    new1.second_name = second_name
    new1.third_name = third_name
    new1.last_name = last_name
    new1.email = email
    new1.mobile = mobile
    #new1.save()

    new2 = models.CssRegister()
    new2.first_name = first_name
    new2.second_name = second_name
    new2.third_name = third_name
    new2.last_name = last_name
    new2.email = email
    new2.mobile = mobile
    #new2.save()

    new3 = models.JsRegister()
    new3.first_name = first_name
    new3.second_name = second_name
    new3.third_name = third_name
    new3.last_name = last_name
    new3.email = email
    new3.mobile = mobile
    #new3.save()

    new4 = models.JqRegister()
    new4.first_name = first_name
    new4.second_name = second_name
    new4.third_name = third_name
    new4.last_name = last_name
    new4.email = email
    new4.mobile = mobile
    #new4.save()

    new5 = models.BootstrapRegister()
    new5.first_name = first_name
    new5.second_name = second_name
    new5.third_name = third_name
    new5.last_name = last_name
    new5.email = email
    new5.mobile = mobile
    #new5.save()

    # newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
    # newc2 = models.Course.objects.get(course_name='CSS / CSS3')
    # newc3 = models.Course.objects.get(course_name='JavaScript')
    # newc4 = models.Course.objects.get(course_name='jQuery')
    # newc5 = models.Course.objects.get(course_name='Bootstrap')
    # newd = models.Department.objects.get(department_name='Front End')

    course1=models.Course.objects.filter(course_name='HTML / HTML 5')
    course2 = models.Course.objects.filter(course_name='CSS / CSS3')
    course3 = models.Course.objects.filter(course_name='JavaScript')
    course4 = models.Course.objects.filter(course_name='jQuery')
    course5 = models.Course.objects.filter(course_name='Bootstrap')

    if course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == True and course5.exists() == True:
        new2.save()
        new3.save()
        new4.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd,'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == True and course5.exists() == True:
        new3.save()
        new4.save()
        new5.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc3.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == True and course5.exists() == True:
        new2.save()
        new4.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == False and course5.exists() == True:
        new2.save()
        new3.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new2.save()
        new3.save()
        new4.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == True:
        new4.save()
        new5.save()
        dd = new4.id

        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new5.save()
        dd = new5.id

        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc5.course_name
        data4 = newd.department_name
        data5 = newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == True:
        new3.save()
        new5.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc3.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new3.save()
        new4.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new2.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new2.save()
        new4.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new2.save()
        new3.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == True:
        new1.save()
        new4.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == True:
        new1.save()
        new3.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new3.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc3.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc3.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new1.save()
        new3.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new1.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new1.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new1.save()
        new3.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc3.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == False and course5.exists() == False:
        new1.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name
        data4 = newd.department_name
        data5 = newc1.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == False:
        new2.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name
        data4 = newd.department_name
        data5 = newc2.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new3.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name
        data4 = newd.department_name
        data5 = newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new4.save()
        dd = new4.id

        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc4.course_name
        data4 = newd.department_name
        data5 = newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new1.save()
        new2.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new1.save()
        new2.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == False:
        new1.save()
        new2.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new1.save()
        new2.save()
        new3.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc3.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new1.save()
        new2.save()
        new3.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
    else:
        new1.save()
        new2.save()
        new3.save()
        new4.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc3.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',{'dd':dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    #except:
     #   msg = 'fill all fields with a correct data'
     #   return render(request, 'frontend/necessarycourses/registerall.html', {'msg': msg})


def allnecessaryupdate(request,id):

    d =models.HtmlRegister.objects.get(id=id) or models.CssRegister.objects.get(id=id) or models.JsRegister.objects.get(id=id) or models.JqRegister.objects.get(id=id) or models.BootstrapRegister.objects.get(id=id)
    data1=d.first_name
    data2=d.second_name
    data3=d.third_name
    data4=d.last_name
    data5=d.email
    data6=d.mobile
    data7=d.id
    return render(request, 'frontend/necessarycourses/allupdate.html', {'st_id':id, 'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5, 'data6':data6, 'data7':data7})



def allnecessarysaveupdate(request,id):

    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    # try:
    new1 = models.HtmlRegister(id=id)
    new1.first_name = first_name
    new1.second_name = second_name
    new1.third_name = third_name
    new1.last_name = last_name
    new1.email = email
    new1.mobile = mobile
    # new1.save()

    new2 = models.CssRegister(id=id)
    new2.first_name = first_name
    new2.second_name = second_name
    new2.third_name = third_name
    new2.last_name = last_name
    new2.email = email
    new2.mobile = mobile
    # new2.save()

    new3 = models.JsRegister(id=id)
    new3.first_name = first_name
    new3.second_name = second_name
    new3.third_name = third_name
    new3.last_name = last_name
    new3.email = email
    new3.mobile = mobile
    # new3.save()

    new4 = models.JqRegister(id=id)
    new4.first_name = first_name
    new4.second_name = second_name
    new4.third_name = third_name
    new4.last_name = last_name
    new4.email = email
    new4.mobile = mobile
    # new4.save()

    new5 = models.BootstrapRegister(id=id)
    new5.first_name = first_name
    new5.second_name = second_name
    new5.third_name = third_name
    new5.last_name = last_name
    new5.email = email
    new5.mobile = mobile
    # new5.save()

    # newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
    # newc2 = models.Course.objects.get(course_name='CSS / CSS3')
    # newc3 = models.Course.objects.get(course_name='JavaScript')
    # newc4 = models.Course.objects.get(course_name='jQuery')
    # newc5 = models.Course.objects.get(course_name='Bootstrap')
    # newd = models.Department.objects.get(department_name='Front End')

    course1 = models.Course.objects.filter(course_name='HTML / HTML 5')
    course2 = models.Course.objects.filter(course_name='CSS / CSS3')
    course3 = models.Course.objects.filter(course_name='JavaScript')
    course4 = models.Course.objects.filter(course_name='jQuery')
    course5 = models.Course.objects.filter(course_name='Bootstrap')

    if course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == True and course5.exists() == True:
        new2.save()
        new3.save()
        new4.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == True and course5.exists() == True:
        new3.save()
        new4.save()
        new5.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc3.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == True and course5.exists() == True:
        new2.save()
        new4.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == False and course5.exists() == True:
        new2.save()
        new3.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new2.save()
        new3.save()
        new4.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == True:
        new4.save()
        new5.save()
        dd = new4.id

        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new5.save()
        dd = new5.id

        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc5.course_name
        data4 = newd.department_name
        data5 = newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == True:
        new3.save()
        new5.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc3.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new3.save()
        new4.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new2.save()
        new5.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new2.save()
        new4.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == False and course2.exists() == True and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new2.save()
        new3.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id) + " - " + str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name + " - " + newc3.course_name
        data4 = newd.department_name
        data5 = newc2.course_price + newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == True:
        new1.save()
        new4.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == True:
        new1.save()
        new3.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new3.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc3.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc3.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new1.save()
        new3.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new1.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new1.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new1.save()
        new3.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc3.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == False and course3.exists() == False and course4.exists() == False and course5.exists() == False:
        new1.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name
        data4 = newd.department_name
        data5 = newc1.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    if course1.exists() == False and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == False:
        new2.save()
        dd = new2.id

        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new2.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc2.course_name
        data4 = newd.department_name
        data5 = newc2.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    if course1.exists() == False and course2.exists() == False and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new3.save()
        dd = new3.id

        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc3.course_name
        data4 = newd.department_name
        data5 = newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    if course1.exists() == False and course2.exists() == False and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new4.save()
        dd = new4.id

        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc4.course_name
        data4 = newd.department_name
        data5 = newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == True:
        new1.save()
        new2.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == False and course4.exists() == True and course5.exists() == False:
        new1.save()
        new2.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == False and course4.exists() == False and course5.exists() == False:
        new1.save()
        new2.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == True and course4.exists() == False and course5.exists() == False:
        new1.save()
        new2.save()
        new3.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new3.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc3.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc3.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    elif course1.exists() == True and course2.exists() == True and course3.exists() == True and course4.exists() == True and course5.exists() == False:
        new1.save()
        new2.save()
        new3.save()
        new4.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc3.course_price + newc4.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
    else:
        new1.save()
        new2.save()
        new3.save()
        new4.save()
        new5.save()
        dd = new1.id

        newc1 = models.Course.objects.get(course_name='HTML / HTML 5')
        newc2 = models.Course.objects.get(course_name='CSS / CSS3')
        newc3 = models.Course.objects.get(course_name='JavaScript')
        newc4 = models.Course.objects.get(course_name='jQuery')
        newc5 = models.Course.objects.get(course_name='Bootstrap')
        newd = models.Department.objects.get(department_name='Front End')

        data1 = str(new1.id) + " - " + str(new2.id) + " - " + str(new3.id) + " - " + str(new4.id) + " - " + str(new5.id)
        data2 = new1.first_name + " " + new1.second_name + " " + new1.third_name + " " + new1.last_name
        data3 = newc1.course_name + " - " + newc2.course_name + " - " + newc3.course_name + " - " + newc4.course_name + " - " + newc5.course_name
        data4 = newd.department_name
        data5 = newc1.course_price + newc2.course_price + newc3.course_price + newc4.course_price + newc5.course_price
        return render(request, 'frontend/necessarycourses/allshow.html',
                      {'dd': dd, 'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

    # except:
    #   msg = 'fill all fields with a correct data'
    #   return render(request, 'frontend/necessarycourses/registerall.html', {'msg': msg})













# #create api first way
# class register_list1(APIView):
#     def get(self,request):   #get ثابتة  self عشان فانكشن داخل كلاس
#         r1=Register.objects.all()   #use serialize  #Register اسم الجدول في مودل
#         r2=jsonregister(r1,many=True)  #jsonregister اسم الكلاس في ملف جاسون
#         return Response(r2.data)  #data محجوزة
#     def post(self):
#         pass
#
# #create api second way
# class register_list2(viewsets.ModelViewSet):
#     queryset = Register.objects.all()    #queryset محجوزة
#     serializer_class = jsonregister      #serializer_class محجوزة
#
#
# class course_list2(viewsets.ModelViewSet):
#     queryset = Course.objects.all()  # queryset محجوزة
#     serializer_class = jsoncourse  # serializer_class محجوزة
