from django.urls import path
from . import views

app_name = "fabrics"
urlpatterns = [
    path("fabrics/", views.ProductListView.as_view(), name="product_list"),
    path("add-fabrics/", views.OrderCreateView.as_view(), name="order_create"),
    path(
        "fabrics/<int:id>/", views.ProductDetailView.as_view(),
        name="cloth_detail"
    ),
]