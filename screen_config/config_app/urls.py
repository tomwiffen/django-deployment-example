from django.conf.urls import re_path
from config_app import views

app_name = 'config_app'

urlpatterns = [
    re_path(r'^new_screen/$', views.new_screen,name='new_screen'),
    re_path(r'^new_panel/$', views.new_panel,name='new_panel'),
]
