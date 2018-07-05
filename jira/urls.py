
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),
    path('project/', include('project.urls')),
    path('employee/', include('employee.urls')),
    path('a/', include('accounts.urls'))
]
