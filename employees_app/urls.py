from django.conf.urls import url
from . import views

app_name = "employees_app"


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^employees/$', views.employees, name='employees'),
    url(r'^employees/add_employee/$', views.add_employee, name='add_employee'),
    url(r'^employees/edit_employee/(?P<id>\d+)/$', views.edit_employee, name='edit_employee'),
]
