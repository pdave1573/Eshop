from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/', views.store, name="store"),
    url(r'^$', views.index, name="index"),
]
