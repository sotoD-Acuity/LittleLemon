from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]