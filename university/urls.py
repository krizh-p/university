from django.urls import path
from . import views

app_name = "university"

urlpatterns = [
    path("", views.index, name='index'),
]
