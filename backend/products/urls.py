from rest_framework.urls import path

from .views import ProductDetailView

urlpatterns = [
    path("<int:pk>/", ProductDetailView.as_view())
]