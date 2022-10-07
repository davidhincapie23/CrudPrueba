from django.urls import path
from . import views

urlpatterns = [

    
    path('', views.listEmpleado),
    path('register/', views.createEmpleado),
    path('edit/<slug:slug>', views.editEmpleado, name='editUrl'),
    path('delete/<slug:slug>', views.deleteEmpleado, name='deleteUrl'),

]