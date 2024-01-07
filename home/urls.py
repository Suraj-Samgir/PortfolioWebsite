#imported from urls.py in portfolio

from django.contrib import admin
from django.urls import path, include # imported include
from home import views

# Django admin header customization

admin.site.site_header = "Login to Developer Suraj"
admin.site.site_title = "Welcom to the Database Page"
admin.site.index_title = "Welcome to This Portal"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name="test"),
]