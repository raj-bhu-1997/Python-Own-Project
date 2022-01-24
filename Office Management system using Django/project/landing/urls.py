
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page.as_view(), name = 'home'),
    path('accounts/', include('allauth.urls')),
]
