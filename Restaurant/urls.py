from django.urls import path
from .views import bookingview,index, menuview,MenuItemsView,SingleMenuItemView

urlpatterns=[
    path('',index,name='index' ),
    path('booking/',bookingview.as_view()),
    path('menu/',menuview.as_view()),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]