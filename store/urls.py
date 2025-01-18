from django.urls import path
from store import views

urlpatterns = [
    path('register/',views.SignupView.as_view(), name="signup"),
    path('',views.SigninView.as_view(), name="signin"),
    path('home/',views.HomeView.as_view(),name="home"),
    path('product/<int:pk>',views.ProductDetailView.as_view(),name="product-detail"),
    path('product/<int:pk>/cart/add/', views.AddTOcartview.as_view(), name="add-to-cart"),
    path('carts/all/',views.CartItemsListView.as_view(),name="cart-list"),
    path('baskets/items/<int:pk>/remove/',views.BasketItemDeleteView.as_view(),name="basket-item-delete"),
    path("basket/item/<int:pk>/quantity/change/",views.BasketItemUpdateQuantityView.as_view(),name="basket-item-qty-update"),
    path("checkout/",views.CheckOutView.as_view(), name="checkout"),
    path("orders/all/",views.MyOrderView.as_view(),name="orders"),
    path('verify/',views.PaymentVerificationView.as_view(),name="verification"),
    path('category/<str:category_name>',views.CategoryListView.as_view(),name="category-list")
    
]