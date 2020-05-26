from django.urls import path
from user_app.views import frontend, backend, android, fullstack, htmlregister, htmlsaveregister, htmlupdate, htmlsaveupdate, htmldelete, cssregister, csssaveregister, cssupdate, csssaveupdate, cssdelete, jsregister, jssaveregister, jsupdate, jssaveupdate, jsdelete, jqregister, jqsaveregister, jqupdate, jqsaveupdate, jqdelete, bootregister, bootsaveregister, bootupdate, bootsaveupdate, bootdelete, allnecessary, allnecessarysave, allnecessaryupdate, allnecessarysaveupdate

urlpatterns = [
    path('frontend/',frontend,name='frontend'),
    path('backend/',backend,name='backend'),
    path('android/',android,name='android'),
    path('fullstack/',fullstack,name='fullstack'),
    ######### html frontend end #################
    path('htmlregister/', htmlregister, name='htmlregister'),
    path('htmlsaveregister/', htmlsaveregister, name='htmlsaveregister'),
    path('htmlupdate/<int:id>/', htmlupdate, name='htmlupdate'),
    path('htmlsaveupdate/<int:id>/', htmlsaveupdate, name='htmlsaveupdate'),
    path('htmldelete/<int:id>/', htmldelete, name='htmldelete'),
    ######### css frontend end #################
    path('cssregister/',cssregister,name='cssregister'),
    path('csssaveregister/', csssaveregister, name='csssaveregister'),
    path('cssupdate/<int:id>/', cssupdate, name='cssupdate'),
    path('csssaveupdate/<int:id>/', csssaveupdate, name='csssaveupdate'),
    path('cssdelete/<int:id>/', cssdelete, name='cssdelete'),
    ######### js frontend end #################
    path('jsregister/',jsregister,name='jsregister'),
    path('jssaveregister/', jssaveregister, name='jssaveregister'),
    path('jsupdate/<int:id>/', jsupdate, name='jsupdate'),
    path('jssaveupdate/<int:id>/', jssaveupdate, name='jssaveupdate'),
    path('jsdelete/<int:id>/', jsdelete, name='jsdelete'),
    ######### jq frontend end #################
    path('jqregister/',jqregister,name='jqregister'),
    path('jqsaveregister/', jqsaveregister, name='jqsaveregister'),
    path('jqupdate/<int:id>/', jqupdate, name='jqupdate'),
    path('jqsaveupdate/<int:id>/', jqsaveupdate, name='jqsaveupdate'),
    path('jqdelete/<int:id>/', jqdelete, name='jqdelete'),
    ######### bootstrap frontend end #################
    path('bootregister/',bootregister,name='bootregister'),
    path('bootsaveregister/', bootsaveregister, name='bootsaveregister'),
    path('bootupdate/<int:id>/', bootupdate, name='bootupdate'),
    path('bootsaveupdate/<int:id>/', bootsaveupdate, name='bootsaveupdate'),
    path('bootdelete/<int:id>/', bootdelete, name='bootdelete'),
    ######### register all necessary front end #########
    path('allnecessary/', allnecessary, name='allnecessary'),
    path('allnecessarysave/', allnecessarysave, name='allnecessarysave'),
    path('allnecessaryupdate/<int:id>/', allnecessaryupdate, name='allnecessaryupdate'),
    path('allnecessarysaveupdate/<int:id>/', allnecessarysaveupdate, name='allnecessarysaveupdate'),
    path('bootdelete/<int:id>/', bootdelete, name='bootdelete'),

]