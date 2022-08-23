
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

]
