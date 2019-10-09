
from django.urls import path
from .views import *


urlpatterns = [
    path('post/', post),
   # path('get_getadmin/<str:name>',get_getadmin)
    path('get/<int:empID>', get)
    # path('justget/', justget)
]