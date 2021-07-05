from django.urls import path, re_path

from . import views
from django.contrib import admin

app_name = 'tournament'
urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    # ex: /tournament/
    path('', views.IndexView.as_view(), name='index'),
]