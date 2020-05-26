from django.urls import re_path
from . import views

app_name = 'shop'

urlpatterns = [
    #product list without any slug
    re_path(r'^$',views.product_list,name='product_list'),
	#product list with any slug
	re_path(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_category'),
	#product detail with id and slug
	re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
]