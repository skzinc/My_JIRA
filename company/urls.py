from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.get_name, name="get_name"),
    path('delete/<int:id>', views.delete, name="delete_entry"),
    path('update_company/<int:id>', views.update, name="update_company"),
]