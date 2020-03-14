from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index , name='index'),
    path('signin/', views.signin , name='signin'),
    path('signup/', views.signup , name='signup') ,
    path('logout/',views.logoutView , name = 'logout'),
    path('dashboard/' , views.dashboard , name ='dashboard'),
    path('dashboard/edit/' , views.edit , name ='edit'),
    path('dashboard/search_projects/' , views.search_projects , name ='search_projects'),
    path('dashboard/requests/',views.requests , name ='requests'),
    path('dashboard/ratings/' , views.ratings , name= 'ratings'),
    path('dashboard/view_projects/add_projects/' , views.add_projects , name ='add_projects'),
    path('dashboard/view_projects/' , views.view_projects , name ='view_projects'),
    path('dashboard/view_projects/join_team/' , views.join_team , name = 'join_team'),
    path('dashboard/view_projects/add_projects/' , views.add_projects , name='add_projects')
]
