from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_data_list),
    path('<int:pk>/', views.person_data_detail),
]