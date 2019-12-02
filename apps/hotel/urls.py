from django.conf.urls import url, include
from apps.hotel.views import index, hotel_view, registro, boot, principal

urlpatterns = [
    url(r'^index/',index, name = 'index'),
    url(r'^nuevo/',hotel_view, name = 'hotel_view'),
    url('registro/',registro ),
    url('boot/',boot ),
    url('principal/',principal ),
]
