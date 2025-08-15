from rest_framework.urls import path

from .views import ProductDetailAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path("<int:pk>/", ProductDetailAPIView.as_view()),
    path("<int:pk>/update/", ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", ProductDestroyAPIView.as_view()),
]