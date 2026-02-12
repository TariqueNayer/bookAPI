from rest_framework import generics, permissions, viewsets


from .models import Book, Order, Order_Status
from .serializers import AdminBookSerializer, OrderSerializer, PublicBookSerializer

# Create your views here.

# Book.

class BookList(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = PublicBookSerializer

class BookView(generics.RetrieveAPIView):
	permission_classes = (permissions.IsAdminUser,)
	queryset = Book.objects.all()
	serializer_class = PublicBookSerializer

class AdminBookListView(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAdminUser,)
	queryset = Book.objects.all()
	serializer_class = AdminBookSerializer

class AdminBookView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAdminUser,)
	queryset = Book.objects.all()
	serializer_class = AdminBookSerializer


# Order.

# renders admin/orders/
class AdminOrderList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAdminUser,)
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

# renders admin/orders/<order_id>/
class AdminOrderView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAdminUser,) 
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

# orders/
class OrderListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        # GET /orders/
        return Order.objects.filter(
            user=self.request.user,
            status__in=[Order_Status.PAID, Order_Status.CANCELLED]
        )

    def perform_create(self, serializer):
        # POST /orders/
        serializer.save(
            user=self.request.user,
            status=Order_Status.PENDING
        )

# orders/<order_id>/
class OrderView(generics.RetrieveAPIView):
	permission_classes = (permissions.IsAuthenticated,) 
	serializer_class = OrderSerializer

	def get_queryset(self):
		return Order.objects.filter(user=self.request.user, status__in=[Order_Status.PAID, Order_Status.CANCELLED])




