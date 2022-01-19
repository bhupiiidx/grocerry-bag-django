
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import *

urlpatterns = [
     path('signup/', signup, name='signup'),
     path('signin/', signin, name='signin'),
     path('signout/', signout, name='signout'),
     path('logout/', logout, name='logout'),
]
