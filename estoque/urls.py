from django.urls import path
from . import views

urlpatterns = [
    path('add_produto/', views.add_produto, name="add_produto"),
    path('update_produto/<slug:slug>/', views.update_produto, name='update_produto'),
]