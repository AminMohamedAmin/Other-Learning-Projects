from django.shortcuts import render
from user_app import models

# Create your views here.

########## login and logout ############
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect


def inlog(request):
    return render(request, 'login.html', {})


def saveinlog(request):
    u = request.POST['username']
    p = request.POST['password']
    result = authenticate(username=u, password=p)
    if result is not None:
        login(request,
              result)  # بيعرفني لو في حد عامل لوجن ع السيستم وانا بسجل بالسوبر يوزر , لو حذفتها عادي بس مش هيعرفني مين اللي عامل لوجن

        if models.Course.objects.filter(course_name='HTML / HTML 5').exists() == True:
            h = models.HtmlRegister.objects.all().count()
            hm = models.Course.objects.get(course_name='HTML / HTML 5').course_price * h
            # return render(request, 'superadminhome.html',{'user': u, 'h': h, 'hm': hm})
        elif models.Course.objects.filter(course_name='HTML / HTML 5').exists() == False:
            h = 0
            hm = 0

        if models.Course.objects.filter(course_name='CSS / CSS3').exists() == True:
            c = models.CssRegister.objects.all().count()
            cm = models.Course.objects.get(course_name='CSS / CSS3').course_price * c
            return render(request, 'superadminhome.html', {'user': u, 'c': c, 'cm': cm})
        elif models.Course.objects.filter(course_name='CSS / CSS3').exists() == False:
            c = 0
            cm = 0

        if models.Course.objects.filter(course_name='JavaScript').exists() == True:
            js = models.JsRegister.objects.all().count()
            jsm = models.Course.objects.get(course_name='JavaScript').course_price * js
            # return render(request, 'superadminhome.html',{'user': u, 'js': js, 'jsm': jsm})
        elif models.Course.objects.filter(course_name='JavaScript').exists() == False:
            js = 0
            jsm = 0

        if models.Course.objects.filter(course_name='jQuery').exists() == True:
            jq = models.JqRegister.objects.all().count()
            jqm = models.Course.objects.get(course_name='jQuery').course_price * jq
            # return render(request, 'superadminhome.html',{'user': u, 'jq': jq, 'jqm': jqm})
        elif models.Course.objects.filter(course_name='jQuery').exists() == False:
            jq = 0
            jqm = 0

        if models.Course.objects.filter(course_name='Bootstrap').exists() == True:
            b = models.BootstrapRegister.objects.all().count()
            bm = models.Course.objects.get(course_name='Bootstrap').course_price * b
            # return render(request, 'superadminhome.html',{'user': u, 'b': b, 'bm': bm})
        elif models.Course.objects.filter(course_name='Bootstrap').exists() == False:
            b = 0
            bm = 0

        return render(request, 'superadminhome.html',
                      {'h': h, 'hm': hm, 'c': c, 'cm': cm, 'js': js, 'jsm': jsm, 'jq': jq, 'jqm': jqm, 'b': b,
                       'bm': bm})
    else:
        return HttpResponse('user is not exist')


# logout
def outlog(request):
    logout(request)
    return HttpResponseRedirect('/')


###################### general ###################

def home(request):
    if models.Course.objects.filter(course_name='HTML / HTML 5').exists() == True:
        h = models.HtmlRegister.objects.all().count()
        hm = models.Course.objects.get(course_name='HTML / HTML 5').course_price * h
        # return render(request, 'superadminhome.html',{'user': u, 'h': h, 'hm': hm})
    elif models.Course.objects.filter(course_name='HTML / HTML 5').exists() == False:
        h = 0
        hm = 0

    if models.Course.objects.filter(course_name='CSS / CSS3').exists() == True:
        c = models.CssRegister.objects.all().count()
        cm = models.Course.objects.get(course_name='CSS / CSS3').course_price * c
        # return render(request, 'superadminhome.html', {'user': u, 'c': c, 'cm': cm})
    elif models.Course.objects.filter(course_name='CSS / CSS3').exists() == False:
        c = 0
        cm = 0

    if models.Course.objects.filter(course_name='JavaScript').exists() == True:
        js = models.JsRegister.objects.all().count()
        jsm = models.Course.objects.get(course_name='JavaScript').course_price * js
        # return render(request, 'superadminhome.html',{'user': u, 'js': js, 'jsm': jsm})
    elif models.Course.objects.filter(course_name='JavaScript').exists() == False:
        js = 0
        jsm = 0

    if models.Course.objects.filter(course_name='jQuery').exists() == True:
        jq = models.JqRegister.objects.all().count()
        jqm = models.Course.objects.get(course_name='jQuery').course_price * jq
        # return render(request, 'superadminhome.html',{'user': u, 'jq': jq, 'jqm': jqm})
    elif models.Course.objects.filter(course_name='jQuery').exists() == False:
        jq = 0
        jqm = 0

    if models.Course.objects.filter(course_name='Bootstrap').exists() == True:
        b = models.BootstrapRegister.objects.all().count()
        bm = models.Course.objects.get(course_name='Bootstrap').course_price * b
        # return render(request, 'superadminhome.html',{'user': u, 'b': b, 'bm': bm})
    elif models.Course.objects.filter(course_name='Bootstrap').exists() == False:
        b = 0
        bm = 0

    return render(request, 'superadminhome.html',
                  {'h': h, 'hm': hm, 'c': c, 'cm': cm, 'js': js, 'jsm': jsm, 'jq': jq, 'jqm': jqm, 'b': b, 'bm': bm})


def front_courses(request):
    data = models.Course.objects.filter(course_dep='front')
    # d=models.Course.objects.get(course_name='HTML / HTML 5').id
    return render(request, 'courses1.html', {'data': data})


def front_update_course(request, id):
    data = models.Course.objects.get(id=id)
    return render(request, 'front_update_course.html', {'student_id': id, 'data': data})


def save_front_update_course(request, id):
    course_dep = request.POST['dep']
    course_name = request.POST['name']
    course_price = request.POST['price']

    new = models.Course(id=id)
    new.course_dep = course_dep
    new.course_name = course_name
    new.course_price = course_price
    new.save()
    return HttpResponseRedirect('../../add_course')


def delete_front_update_course(request, id):
    old = models.Course(id=id)
    old.delete()
    return HttpResponseRedirect('../../add_course')


def front_projects(request):
    data = models.Project.objects.filter(project_dep='front')
    return render(request, 'projects1.html', {'data': data})


def front_update_project(request, id):
    data = models.Project.objects.get(id=id)
    return render(request, 'front_update_project.html', {'student_id': id, 'data': data})


def save_front_update_project(request, id):
    project_dep = request.POST['dep']
    project_name = request.POST['name']
    project_price = request.POST['price']

    new = models.Project(id=id)
    new.project_dep = project_dep
    new.project_name = project_name
    new.project_price = project_price
    new.save()
    return HttpResponseRedirect('../../add_project')


def delete_front_update_project(request, id):
    old = models.Project(id=id)
    old.delete()
    return HttpResponseRedirect('../../add_project')


def front_students(request):
    if models.Department.objects.filter(department_name='Front End').exists():
        if models.Course.objects.filter(course_name='HTML / HTML 5').exists() == True:
            h = models.HtmlRegister.objects.all().count()
            hm = models.Course.objects.get(course_name='HTML / HTML 5').course_price * h
        elif models.Course.objects.filter(course_name='HTML / HTML 5').exists() == False:
            h = 0
            hm = 0

        if models.Course.objects.filter(course_name='CSS / CSS3').exists() == True:
            c = models.CssRegister.objects.all().count()
            cm = models.Course.objects.get(course_name='CSS / CSS3').course_price * c
        elif models.Course.objects.filter(course_name='CSS / CSS3').exists() == False:
            c = 0
            cm = 0

        if models.Course.objects.filter(course_name='JavaScript').exists() == True:
            js = models.JsRegister.objects.all().count()
            jsm = models.Course.objects.get(course_name='JavaScript').course_price * js
        elif models.Course.objects.filter(course_name='JavaScript').exists() == False:
            js = 0
            jsm = 0

        if models.Course.objects.filter(course_name='jQuery').exists() == True:
            jq = models.JqRegister.objects.all().count()
            jqm = models.Course.objects.get(course_name='jQuery').course_price * jq
        elif models.Course.objects.filter(course_name='jQuery').exists() == False:
            jq = 0
            jqm = 0

        if models.Course.objects.filter(course_name='Bootstrap').exists() == True:
            b = models.BootstrapRegister.objects.all().count()
            bm = models.Course.objects.get(course_name='Bootstrap').course_price * b
        elif models.Course.objects.filter(course_name='Bootstrap').exists() == False:
            b = 0
            bm = 0
        all=h+c+js+jq+b
        sum=hm+cm+jsm+jqm+bm
        return render(request, 'students1.html',
                      {'h': h, 'hm': hm, 'c': c, 'cm': cm, 'js': js, 'jsm': jsm, 'jq': jq, 'jqm': jqm, 'b': b, 'bm': bm,'all':all, 'sum':sum})
    else:
        return HttpResponse('department is not available')

def front_students_html_list(request):
    data=models.HtmlRegister.objects.all()
    return render(request, 'student_html_list.html', {'data':data})



def front_programmers(request):
    data = models.programmers.objects.filter(prog_dep='front')
    return render(request, 'programmers1.html', {'data': data})



################## extra ##############

def add_course(request):
    data = models.Course.objects.all()
    return render(request, 'add_course.html', {'data': data})


def save_course(request):
    course_dep = request.POST['dep']
    course_name = request.POST['name']
    course_price = request.POST['price']

    new = models.Course()
    new.course_dep = course_dep
    new.course_name = course_name
    new.course_price = course_price
    new.save()
    return HttpResponseRedirect('../add_course')


def add_dep(request):
    data = models.Department.objects.all()
    return render(request, 'add_dep.html', {'data': data})


def save_dep(request):
    department_name = request.POST['name']

    new = models.Department()
    new.department_name = department_name
    new.save()
    return HttpResponseRedirect('../add_dep')


def add_admin(request):
    data = User.objects.all()
    return render(request, 'add_admin.html', {'data': data})


def save_admin(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    return HttpResponseRedirect('../add_admin')


def add_project(request):
    data = models.Project.objects.all()
    return render(request, 'add_project.html', {'data': data})


def save_project(request):
    project_dep = request.POST['dep']
    project_name = request.POST['name']
    project_price = request.POST['price']

    new = models.Project()
    new.project_dep = project_dep
    new.project_name = project_name
    new.project_price = project_price
    new.save()
    return HttpResponseRedirect('../add_project')


def add_prog(request):
    data = models.programmers.objects.all()
    return render(request, 'add_prog.html', {'data': data})


def save_prog(request):
    prog_dep = request.POST['dep']
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    third_name = request.POST['third_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    address1 = request.POST['address1']
    address2 = request.POST['address2']
    address3 = request.POST['address3']
    address4 = request.POST['address4']
    # front_id_card=request.POST.FILES['front_id']
    # back_id_card = request.POST.FILES['back_id']
    new = models.programmers()
    new.prog_dep=prog_dep
    new.first_name = first_name
    new.second_name = second_name
    new.third_name = third_name
    new.last_name = last_name
    new.email = email
    new.mobile = mobile
    new.address1 = address1
    new.address2 = address2
    new.address3 = address3
    new.address4 = address4
    # new.front_id_card = front_id_card
    # new.back_id_card = back_id_card
    new.save()
    return HttpResponseRedirect('../add_prog')
