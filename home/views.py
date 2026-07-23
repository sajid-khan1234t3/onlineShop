from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product, Cart, Order,Wishlist


def home(request):
    search = request.GET.get("search")

    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    return render(request, "home/index.html", {
        "products": products
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "home/product_detail.html", {
        "product": product
    })


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


def cart(request):
    items = Cart.objects.all()
    total = sum(item.total_price() for item in items)

    return render(request, "home/cart.html", {
        "items": items,
        "total": total,
    })
def remove_from_cart(request, id):
    item = get_object_or_404(Cart, id=id)
    item.delete()
    return redirect("cart")


def increase_quantity(request, id):
    item = get_object_or_404(Cart, id=id)
    item.quantity += 1
    item.save()
    return redirect("cart")


def decrease_quantity(request, id):
    item = get_object_or_404(Cart, id=id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")

def checkout(request):
    if request.method == "POST":

        items = Cart.objects.all()

        for item in items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                customer_name=request.POST["customer_name"],
                phone=request.POST["phone"],
                address=request.POST["address"],
                payment_method=request.POST["payment_method"],
                status="Pending"
            )

        items.delete()

        return redirect("orders")

    return render(request, "home/checkout.html")


def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "home/orders.html", {
        "orders": orders
    })


def contact(request):
    return render(request, "home/contact.html")
def add_to_wishlist(request, id):
    if not request.user.is_authenticated:
        return redirect("login")

    product = get_object_or_404(Product, id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("home")
def remove_from_wishlist(request, id):
    wishlist_item = get_object_or_404(
        Wishlist,
        id=id
    )

    wishlist_item.delete()

    return redirect("wishlist")


def wishlist(request):
    if not request.user.is_authenticated:
        return redirect("login")

    items = Wishlist.objects.filter(user=request.user)

    return render(request, "home/wishlist.html", {
        "items": items
    })
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "home/signup.html", {
                "error": "Username already exists"
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("login")

    return render(request, "home/signup.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("profile")

        return render(request, "home/login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "home/login.html")


def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "home/profile.html")


def logout_user(request):
    logout(request)
    return redirect("home")