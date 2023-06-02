from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Todo import views

urlpatterns = [
    url(r'^task$',views.taskApi),
    url(r'^task$',views.taskApi),
    url(r'^task/([0-9]+)$',views.taskApi),
    path('admin/', admin.site.urls),
]