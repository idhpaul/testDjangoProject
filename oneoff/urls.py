from django.urls import path

from . import views

urlpatterns = [
    path('apikey', views.apikey, name="apikey"),
    path('foo', views.foo, name="foo"),
    path('bar', views.bar, name="bar"),
]