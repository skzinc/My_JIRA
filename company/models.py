from django.db import models

company_categories = (
    ('finance', 'Finance'),
    ('consulting', 'Consulting'),
    ('data analytics', 'Data Analytics'),
    ('construction', 'Contruction'),
    ('mining', 'Mining'),
    ('oil and gas', 'Oil and Gas'),
    ('IT', 'IT'),
    ('business', 'Business'),
    ('services', 'Services'),
    ('others', 'Others'),
)
class Company(models.Model):
    c_name = models.CharField(max_length=250, blank=False)
    c_location = models.CharField(max_length=250, blank=False)
    c_code = models.CharField(max_length=250, blank=False, unique=True)
    c_category = models.CharField(max_length=250, blank=False, choices=company_categories)
    c_projects = models.CharField(max_length=250, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    c_description = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return self.c_name



