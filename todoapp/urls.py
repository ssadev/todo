from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/<str:item>/', views.add, name="add"),
    path('dlt/<int:itemId>/', views.dlt, name="dlt"),

]
