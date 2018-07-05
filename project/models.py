from django.db import models
from employee.models import Employee

class Project(models.Model):
    company = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=250, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    project_code = models.CharField(max_length=250, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project_Modules(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    m_code = models.CharField(max_length=250, blank=False, unique=True)
    name = models.CharField(max_length=250, blank=False)
    employee = models.ManyToManyField(Employee, verbose_name="list of employees")
    assign = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignee', null=True)
    end_date = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

