from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import bookingview,index, menuview,MenuItemsView,SingleMenuItemView,SingleBookingItemView,SingleMenuItemView

urlpatterns=[
    path('',index,name='index' ),
    path('booking/',bookingview.as_view()),
    path('booking/<int:pk>',SingleBookingItemView.as_view()),
    path('menu/',menuview.as_view()),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)

]