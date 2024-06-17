from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product
from .forms import UserRegisterForm
from django.urls import reverse, reverse_lazy

from .models import Cart, CartItem


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect(reverse('login'))
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")


@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart_detail')
    else:
        # Если метод запроса не POST, редиректим пользователя обратно на страницу товара или на главную
        return redirect('product_list')



@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart_detail.html', {'cart': cart})


