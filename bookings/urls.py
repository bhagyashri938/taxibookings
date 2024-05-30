from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('taxis/', views.taxi_list, name='taxi_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('receipts/', views.receipt_list, name='receipt_list'),
    path('taxis/create/', views.create_taxi, name='create_taxi'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('receipts/create/', views.create_receipt, name='create_receipt'),
]

