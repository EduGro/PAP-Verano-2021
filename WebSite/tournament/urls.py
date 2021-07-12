from django.urls import path, re_path

from . import views
from django.contrib import admin
from django.urls import include

app_name = 'tournament'
urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    # ex: /tournament/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /tournament/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]