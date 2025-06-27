from django.urls import path
from .views import CreateTransactionView, VerifyTransactionView

urlpatterns = [
    path('create/', CreateTransactionView.as_view(), name='transaction-create'),
    path('verify/', VerifyTransactionView.as_view(), name='transaction-verify'),
]