import imp
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path(
        'prueba/', 
        views.IndexView.as_view(),
        name='home'
        ),

    path(
        'lista/', 
        views.PruebaListView.as_view(),
        name='lista',

        ),
    path(
        'add/', 
        views.PruebaCreateView.as_view(), 
        name='prueba_add',
        ), 
    path(
        'resume-foundation/', 
        views.ResumeFoundationView.as_view(), 
        name='resume_foundation',
        ),        
]