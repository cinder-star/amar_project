from django.urls import path

from . import views

urlpatterns = [
    path("", views.recorder, name="recorder"),
    path("send/", views.record, name="record"),
    path("get_new_sentence/", views.new_sentence, name="new_sentence"),
]
