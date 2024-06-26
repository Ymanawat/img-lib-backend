from django.conf import settings
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('upload', views.createImage, name='uploadImage'),
    re_path('retrieve', views.retrieve_images_by_tags, name='retrieveImages'),

]


