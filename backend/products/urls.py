from rest_framework.urls import path

from .views import ProductDetailAPIView, ProductListCreateAPIView

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path("<int:pk>/", ProductDetailAPIView.as_view()),
]