
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from bag.views import *

urlpatterns = [
     path('', homepage, name='home'),
     path('/', homepage, name='homeslash'),
     path('add-item/', add_item, name='add-item'),
     path('update-item/<int:item_id>/', update_item, name='update-item'),
     path('delete-item/<int:item_id>/', delete_item, name='delete-item'),
]
