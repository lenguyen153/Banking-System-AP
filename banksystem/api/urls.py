from django.urls import path
# from django.conf.urls import url
from rest_framework import routers

from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BanksAPIView,
    # BankDetailAPIView,
    # CreateAccountAPIView,
    # AccountListAPIView
)


# router = routers.SimpleRouter()
# router.register(r'branches', BranchesAPIView, basename='branches')
# router.register(r'branch', BranchDetailAPIView, basename='branch-detail')
# router.register(r'banks', BanksAPIView, basename='banks')
# router.register(r'bank', BankDetailAPIView, basename='bank-detail')
# router.register(r'create_account', CreateAccountAPIView, basename='create-account')
# router.register(r'accounts', AccountListAPIView, basename='accounts')

urlpatterns = [
    # url(r'api/branch/(?P<pk>[0-9]+)/', BranchDetailAPIView.as_view(), name='branch-detail'),
    # url(r'api/branches/', BranchesAPIView.as_view(), name='branches'),
    # url(r'api/banks/', BanksAPIView.as_view(), name = 'banks'),
    path(r'branch/<int:pk>/', BranchDetailAPIView.as_view(), name='branch-detail'),
    path(r'branches/', BranchesAPIView.as_view(), name='branches'),
    path(r'banks/', BanksAPIView.as_view(), name='banks')
]
