from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    FridgeListView,
    FridgeDetailView,
    FridgeCreateView,
)
from . import views


urlpatterns = [
    # path('', views.home, name='fridge-home'),
    path('', ItemListView.as_view(), name='fridge-home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('', FridgeListView.as_view(), name='fridge-home'),
    path('Fridge/<int:pk>/', FridgeDetailView.as_view(), name='fridge-detail'),
    path('item/new/', FridgeCreateView.as_view(), name='fridge-create'),
    path('about/', views.about, name='fridge-about'),
]




