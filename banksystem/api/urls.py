from django.urls import path
# from django.conf.urls import url
from rest_framework import routers

from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BanksAPIView,
    BankDetailAPIView,
    CreateAccountAPIView,
    AccountListAPIView
)

urlpatterns = [
    path(r'branch/<int:pk>/', BranchDetailAPIView.as_view(), name='branch-detail'),
    path(r'branches/', BranchesAPIView.as_view(), name='branches'),
    path(r'banks/', BanksAPIView.as_view(), name='banks'),
    path(r'branch/<int:pk>/', BankDetailAPIView.as_view(), name='bank-detail'),
    path(r'create_account/', CreateAccountAPIView.as_view(), name='create-account'),
    path(r'accounts/', AccountListAPIView.as_view(), name='accounts')
]
