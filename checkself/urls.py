from django.urls import path

from . import views

urlpatterns = [
    path('wake', views.wake, name="self"),
    path('auth', views.auth, name="self"),
    path('self', views.self, name="self"),
    path('foo', views.foo, name="foo"),
]