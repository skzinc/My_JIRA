from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('p_entry/', views.project_form, name="project"),
    path('pm_entry/', views.p_module_form, name="p_module"),
    path('delete/<int:id>', views.delete_project, name="delete_project_entry"),
    path('delete_module/<int:id>', views.delete_module, name="delete_module_entry"),
]
