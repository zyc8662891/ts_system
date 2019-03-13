"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appo import views
urlpatterns = [
    url(r'^$',views.home),
    url(r'^show_login/$',views.show_login,name='show_login'),
    url(r'^show_author/$',views.show_author, name='show_author'),
    url(r'^show_book/$',views.show_book,name='show_book'),
    url(r'^show_publish/$',views.show_publish,name='show_publish'),
    url(r'^update_book/$',views.update_book,name='update_book'),
    url(r'^add_book/$',views.add_book,name='add_book'),
    url(r'^update_author/$',views.update_author,name='update_author'),
    url(r'^add_author/$',views.add_author,name='add_author'),
    url(r'^update_publish/$',views.update_publish,name='update_publish'),
    url(r'^add_publish/$',views.add_publish,name='add_publish'),
    url(r'^delete_book/(?P<book_id>\d+)/$',views.delete_book,name='delete_book'),
    url(r'^delete_author/(?P<author_id>\d+)/$',views.delete_author,name='delete_author'),
    url(r'^delete_publish/(?P<publish_id>\d+)/$',views.delete_publish,name='delete_publish'),
    url(r'^login_out/$',views.logout,name='logout'),
    url(r'add_session/$',views.add_session)
    
















]
