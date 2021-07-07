from django.urls import path, re_path

from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

app_name = 'principal'
urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    # ex: //
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]