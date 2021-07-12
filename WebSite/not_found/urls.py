from django.urls import path, re_path

from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView

app_name = 'not_found'
urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    # ex: /not_found/
    path('', TemplateView.as_view(template_name='not_found.html'), name='index'),
]