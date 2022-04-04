from django.urls import path
from .views import RegistrUserView, add_balance_view, \
    get_balance_view, sub_balance_view, get_overall_balance_view, get_0_users_view, get_1000_users_view

urlpatterns = [
    path('registr/', RegistrUserView.as_view(), name='registr'),
    path('add/', add_balance_view),
    path('sub/', sub_balance_view),
    path('balance/', get_balance_view),
    path('all_balance/', get_overall_balance_view),
    path('all_0/', get_0_users_view),
    path('all_1000/', get_1000_users_view),
]