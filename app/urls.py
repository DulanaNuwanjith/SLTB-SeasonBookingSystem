from django.urls import path 
from app.views import StudentCreateView , StudentListView , StudentDetailView
from app.views import SeasonCreateView , SeasonListView 
from app.views import PrincipalCreateView  , PrincipalListView 
from app import views
from app.views import About , Contact , Service

urlpatterns = [

    path('studentcreateview', StudentCreateView.as_view()),
    path('studentlistview', StudentListView.as_view()),
    path('studentdetailveiw/<int:pk>', StudentDetailView.as_view()),

    path('seasoncreateview', SeasonCreateView.as_view()),
    path('seasonlistview', SeasonListView.as_view()),

    path('principalcreateview', PrincipalCreateView.as_view()),
    path('principallistview', PrincipalListView.as_view()),
    path('about', views.About),
    path('contact', views.Contact),
    path('service', views.Service),
    
]