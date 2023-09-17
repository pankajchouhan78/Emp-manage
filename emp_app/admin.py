from django.contrib import admin

#from .models import Department,Role,Employee
from emp_app.models import Department,Role,Employee
# Register your models here.
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)
