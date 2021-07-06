from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoeboxListView.as_view(), name='box-list'),
    path('box/<int:pk>/', views.ShoeboxDetailView.as_view(), name='box-detail'),
    path('add/', views.ShoeboxCreateView.as_view(), name="box-create"),
]