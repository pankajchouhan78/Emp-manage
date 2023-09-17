from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    
    path('view_all_emp',views.view_all_emp,name="view_all_emp"),

    path('add_amp',views.add_amp,name="add_amp"),

    path('remove_emp',views.remove_emp,name="remove_emp"),
    
    path('remove_emp/<int:emp_id>',views.remove_emp,name="remove_emp"),

    path('filter_emp',views.filter_emp,name="filter_emp"),
]
