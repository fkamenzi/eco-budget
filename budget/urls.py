from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('purchase_history/', views.purchase_history, name='purchase_history'),
     path('transactions/', views.transactions_view, name='transactions'),
     path('add_category/', views.add_category, name='add_category'),
     path("transactions/delete/<int:transaction_id>/", views.delete_transaction, name="delete_transaction"),

]
