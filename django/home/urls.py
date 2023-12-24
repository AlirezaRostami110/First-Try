from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:st_id>/', views.detail, name='details'),
    path('delete/<int:st_id>/', views.delete, name='delete'),
    path('update/<int:st_id>/', views.update, name='update'),
    path('create/', views.create, name='create'),
]