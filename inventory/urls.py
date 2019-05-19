from django.conf.urls import url
from . import views

app_name = "inventory"

urlpatterns = [
    url(r'^product_list', views.ProductView.list, name='product_list'),
    url(r'^product_create', views.ProductView.create, name='product_create'),
    url(r'^product_save', views.ProductView.save, name='product_save'),
    url(r'^customer_list',views.CustomerView.list,name='customer_list'),
    url(r'^customer_detail/(?P<id>[\w\-]+)/$',views.CustomerView.detail,name='customer_detail'),
    url(r'^category_list',views.CategoryView.list,name='category_list'),
    url(r'^category_edit/(?P<id>[\w\-]+)/$',views.CategoryView.edit,name='category_edit'),
    url(r'^category_save',views.CategoryView.save,name='category_save'),
    url(r'^category_create',views.CategoryView.create,name='category_create'),

    ]