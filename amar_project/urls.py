from django.urls import path

from . import views

urlpatterns = [
    path("", views.recorder, name="recorder"),
    path("send/", views.record, name="record"),
]
