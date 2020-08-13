from django.urls import path, include
from rest_framework import routers
from . import views
import snippets
app_name = 'accounts'


urlpatterns = [
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),

]