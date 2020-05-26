
from django.urls import path
from .views import inlog,saveinlog,home,outlog,front_courses,add_course,save_course,add_dep,save_dep,add_admin,save_admin,add_project,save_project,add_prog,save_prog, front_update_course, save_front_update_course,delete_front_update_course
from .views import front_projects, front_update_project, save_front_update_project,delete_front_update_project
from .views import front_students, front_students_html_list
from .views import front_programmers

urlpatterns = [
    path('inlog/',inlog,name='inlog'),
    path('saveinlog/',saveinlog,name='saveinlog'),
    path('home/',home,name='home'),
    path('outlog/',outlog,name='outlog'),
    path('add_course/',add_course,name='add_course'),
    path('save_course/',save_course,name='save_course'),
    path('add_dep/',add_dep,name='add_dep'),
    path('save_dep/',save_dep,name='save_dep'),
    path('add_admin/',add_admin,name='add_admin'),
    path('save_admin/',save_admin,name='save_admin'),
    path('add_project/',add_project,name='add_project'),
    path('save_project/',save_project,name='save_project'),
    path('add_prog/',add_prog,name='add_prog'),
    path('save_prog/',save_prog,name='save_prog'),

    path('front_courses/',front_courses,name='front_courses'),
    path('front_update_course/<int:id>/',front_update_course,name='front_update_course'),
    path('save_front_update_course/<int:id>/',save_front_update_course,name='save_front_update_course'),
    path('delete_front_update_course/<int:id>/', delete_front_update_course, name='delete_front_update_course'),

    path('front_projects/',front_projects,name='front_projects'),
    path('front_update_project/<int:id>/',front_update_project,name='front_update_project'),
    path('save_front_update_project/<int:id>/',save_front_update_project,name='save_front_update_project'),
    path('delete_front_update_project/<int:id>/', delete_front_update_project, name='delete_front_update_project'),

    path('front_students/', front_students, name='front_students'),
    path('front_students_html_list/', front_students_html_list, name='front_students_html_list'),

    path('front_programmers/', front_programmers, name='front_programmers'),

]