from django.conf.urls import url
from . import views

app_name = "administration"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^user_logout/', views.user_logout, name='user_logout'),

    url(r'^learn_page_list', views.LearnPageView.list, name='learn_page_list'),
    url(r'^learn_page_edit/(?P<id>[\w\-]+)/$', views.LearnPageView.edit, name='learn_page_edit'),
    url(r'^learn_page_save', views.LearnPageView.save, name='learn_page_save'),
    url(r'^learn_page_create', views.LearnPageView.create, name='learn_page_create'),

    url(r'^about_page_list', views.AboutPageView.list, name='about_page_list'),
    url(r'^about_page_edit/(?P<id>[\w\-]+)/$', views.AboutPageView.edit, name='about_page_edit'),
    url(r'^about_page_save', views.AboutPageView.save, name='about_page_save'),
    url(r'^about_page_create', views.AboutPageView.create, name='about_page_create'),
]