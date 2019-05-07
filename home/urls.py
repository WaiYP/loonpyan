from django.conf.urls import url
from . import views

app_name = "home"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^product/$',views.product,name='product'),
    url (r'^activities/$',views.activities,name='activities'),
    url (r'^productdetail/$',views.productdetail,name='productdetail'),
    url(r'^contact/$', views.contact, name='contact'),
]