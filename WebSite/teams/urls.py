from django.urls import path, re_path

from . import views
from django.contrib import admin

app_name = 'teams'
urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    # ex: /teams/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /teams/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]