from django.urls import path

from . import views

urlpatterns = [
    path('self', views.self, name="self"),
    path('foo', views.foo, name="foo"),
]