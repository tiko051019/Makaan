from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegisterPage,name='register'),
    path('login/',LoginPage,name='login'),
    path('logout/',Logout,name='logout'),
    #----------------------------------------------
    path('',HomeListView.as_view(),name='home'),
    path('about/',AboutListView.as_view(),name='about'),
    path('pr_list/',PropertyListView.as_view(),name = 'pr_list'),
    path('contact/',ContactPage.as_view(),name = 'contact'),
    path('search/',SearchItem,name='search'),
    
]