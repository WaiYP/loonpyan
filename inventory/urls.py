from django.conf.urls import url
from . import views

app_name = "inventory"

urlpatterns = [
    url(r'^product_list', views.ProductView.list, name='product_list'),
    url(r'^product_edit/(?P<id>[\w\-]+)/$', views.ProductView.edit, name='product_edit'),
    url(r'^product_create', views.ProductView.create, name='product_create'),
    url(r'^product_save', views.ProductView.save, name='product_save'),

    url(r'^customer_list',views.CustomerView.list,name='customer_list'),
    url(r'^customer_detail/(?P<id>[\w\-]+)/$',views.CustomerView.detail,name='customer_detail'),

    url(r'^category_list',views.CategoryView.list,name='category_list'),
    url(r'^category_edit/(?P<id>[\w\-]+)/$',views.CategoryView.edit,name='category_edit'),
    url(r'^category_save',views.CategoryView.save,name='category_save'),
    url(r'^category_create',views.CategoryView.create,name='category_create'),

    url(r'^pgroup_list', views.PgroupView.list, name='pgroup_list'),
    url(r'^pgroup_edit/(?P<id>[\w\-]+)/$', views.PgroupView.edit, name='pgroup_edit'),
    url(r'^pgroup_save', views.PgroupView.save, name='pgroup_save'),
    url(r'^pgroup_create', views.PgroupView.create, name='pgroup_create'),

    url(r'^psubgroup_list', views.PsubgroupView.list, name='psubgroup_list'),
    url(r'^psubgroup_edit/(?P<id>[\w\-]+)/$', views.PsubgroupView.edit, name='psubgroup_edit'),
    url(r'^psubgroup_save', views.PsubgroupView.save, name='psubgroup_save'),
    url(r'^psubgroup_create', views.PsubgroupView.create, name='psubgroup_create'),

    url(r'^actgroup_list', views.ActivityGroupView.list, name='actgroup_list'),
    url(r'^actgroup_edit/(?P<id>[\w\-]+)/$', views.ActivityGroupView.edit, name='actgroup_edit'),
    url(r'^actgroup_save', views.ActivityGroupView.save, name='actgroup_save'),
    url(r'^actgroup_create', views.ActivityGroupView.create, name='actgroup_create'),

    url(r'^activity_list', views.ActivityView.list, name='activity_list'),
    url(r'^activity_edit/(?P<id>[\w\-]+)/$', views.ActivityView.edit, name='activity_edit'),
    url(r'^activity_save', views.ActivityView.save, name='activity_save'),
    url(r'^activity_create', views.ActivityView.create, name='activity_create'),

    url(r'^sergroup_list', views.ServiceGroupView.list, name='sergroup_list'),
    url(r'^sergroup_edit/(?P<id>[\w\-]+)/$', views.ServiceGroupView.edit, name='sergroup_edit'),
    url(r'^sergroup_save', views.ServiceGroupView.save, name='sergroup_save'),
    url(r'^sergroup_create', views.ServiceGroupView.create, name='sergroup_create'),

]