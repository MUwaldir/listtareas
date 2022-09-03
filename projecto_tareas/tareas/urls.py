from unicodedata import name
from django.urls import path
from tareas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about , name='about'),
    path('listtareas', views.listtareas , name='listtareas'),
    path('insert' , views.insert , name='insert'),
    path('delete/<int:task_id>', views.delete , name='delete'),
    path('update/<int:task_id>', views.update_form , name='update_form'),
    path('update', views.update, name='update')
    
]
