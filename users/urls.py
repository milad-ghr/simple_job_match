from django.urls import path

from .views import AccountAPIView

urlpatterns = [
    path('', AccountAPIView.as_view(), name='accounts_list'),
    path('<int:id>/', AccountAPIView.as_view(), name='account'),
]
