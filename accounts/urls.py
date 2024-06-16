from django.urls import path
from .views import register, CustomLoginView, profile, AuthLogoutView, cart_detail, add_to_cart

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('cart/', cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),

]