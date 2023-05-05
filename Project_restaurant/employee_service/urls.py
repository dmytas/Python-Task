from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/', views.register_employee, name='register_employee'),
]
