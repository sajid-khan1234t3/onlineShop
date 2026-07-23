from django.contrib import admin
from .models import Product, Cart, Order, Wishlist


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "product",
        "quantity",
        "payment_method",
        "status",
    )

    list_filter = ("status", "payment_method")
    search_fields = ("customer_name", "phone")

    # Status ko order list se direct change karne ke liye
    list_editable = ("status",)


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")