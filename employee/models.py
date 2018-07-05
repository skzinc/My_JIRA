from django.db import models

employee_roles = (
    ('admin', 'Admin'),
    ('TL', 'Team Leader'),
    ('emp', 'Employee'),
)

gender = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class Employee(models.Model):
    name = models.CharField(max_length=250, blank=False)
    age = models.CharField(max_length=250, blank=False)
    gender = models.CharField(max_length=6, blank=False, default='M', choices=gender)
    code = models.CharField(max_length=250, unique=True, blank=False)
    email = models.CharField(max_length=250, unique=True, blank=False)
    mobile = models.CharField(max_length=12, blank=False)
    salary = models.CharField(max_length=260,blank=False)
    role = models.CharField(max_length=25, blank=False, choices= employee_roles)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name