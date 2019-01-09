"""workshop3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from booking.views import newRoom,modifyRoom,deleteRoom,room,allRooms,newBooking,allBookings,modifyBooking,deleteBooking,search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newRoom',newRoom.as_view(),name='newRoom'),
    path('allRooms',allRooms.as_view(),name='allRooms'),
    path('modifyRoom/<int:id>', modifyRoom.as_view(), name='modifyRoom'),
    path('deleteRoom/<int:id>', deleteRoom.as_view(), name='deleteRoom'),
    path('room/<int:id>', room.as_view(),name='room'),
    path('newBooking/<int:id>', newBooking.as_view(),name='newBooking'),
    path('newBooking', newBooking.as_view(),name='newBooking'),
    path('allBookings', allBookings.as_view(),name='allBookings'),
    #path('modifyBooking/<int:id>', modifyBooking.as_view(), name='modifyBooking'),
    path('deleteBooking/<int:id>', deleteBooking.as_view(), name='deleteBooking'),
    re_path(r'^modifyBooking/(?P<id>[0-9]+)/(?P<room>[0-9]+)$',modifyBooking.as_view(),name='modifyBooking'),
    path('search', search.as_view(),name='search'),
]
