from django.urls import path
from .views import page
from page import views

urlpatterns = [
    path('', views.page, name="page")
]