from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('laptops/', views.LaptopsListView.as_view(), name='laptops'),
    path('laptops/<int:id>/', views.LaptopsDetailView.as_view(), name='laptop_detail'),
    path('store-description/', views.store_description, name='store_description'),
    path('computers/', views.ComputerListView.as_view(), name='computers'),
    path('computers/<int:id>/', views.ComputerDetailView.as_view(), name='pc_detail'),

]