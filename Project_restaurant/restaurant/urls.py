from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from employee_service.views import home, register_employee
from menu_service.views import menu
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('employee/', register_employee, name='register_employee'),
    path('menu/', menu, name='menu'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
