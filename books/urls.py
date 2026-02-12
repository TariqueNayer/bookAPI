from django.urls import path
from . import views


urlpatterns [
    # Books (Public)
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookView.as_view(), name="book-detail"),

    # Books (Admin)
    path("admin/books/", views.AdminBookListView.as_view(), name="admin-book-list"),
    path("admin/books/<int:pk>/", views.AdminBookView.as_view(), name="admin-book-detail"),

    # Orders (User)
    path("orders/", views.OrderListCreateView.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", views.OrderView.as_view(), name="order-detail"),
    
    # Orders (Admin)
    path("admin/orders/", views.AdminOrderList.as_view(), name="admin-order-list"),
    path("admin/orders/<int:pk>/", views.AdminOrderView.as_view(), name="admin-order-detail"),
]