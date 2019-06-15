from django.conf.urls import url
from . import views

app_name = "home"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^product/(?P<pgrpid>\d+)/(?P<psubgrpid>\d+)/$',views.product,name='product'),
    url (r'^activities/(?P<actgrp>\d+)/$',views.activities,name='activities'),
    url (r'^productdetail/(?P<pid>\d+)/$',views.productdetail,name='productdetail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^customer_save/$',views.custsave,name='customer_save'),
    url(r'^productshow/(?P<pgrpid>\d+)/(?P<psubgrpid>\d+)/$',views.productshow,name='productshow'),
]