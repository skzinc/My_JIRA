from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.employee_form, name="employee_form"),
    path('delete/<int:id>', views.delete, name="delete_entry"),
]