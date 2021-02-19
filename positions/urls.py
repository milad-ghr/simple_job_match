from django.urls import path

from .views import PositionsAPIView

urlpatterns = [
    path('', PositionsAPIView.as_view(), name='positions_list'),
    path('<int:id>/', PositionsAPIView.as_view(), name='position'),
]
