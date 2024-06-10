from django.urls import path
from . import views
from .views import get_all_employees
from .views import add_employees

urlpatterns = [
    path("",views.index,name="index"),
    path("getEmployees",get_all_employees,name="get_all_employees"),
    path("addEmployees",add_employees,name="add_employees")
]