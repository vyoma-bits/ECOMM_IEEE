from django.contrib import admin
from django.urls import path
from . import views
from shop import views
urlpatterns = [
path('to/',views.index,name='index'),
path('about/', views.about,name="AboutUs"),
path('contact/', views.contact,name="ContactUs"),
path('tracker', views.tracker,name="TrackingStatus"),
path('search/', views.search,name="Search"),
path('productview/', views.productView,name="TrackingStatus"),
path('checkout/', views.checkout,name="Checkout"),





path('',views.SignupPage,name='signup'),
 path('login/',views.LoginPage,name='login'),
path('logout/',views.LogoutPage,name='logout'),






    
]

