from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

name_app = 'snippets'

urlpatterns = [
    # path('', views.snippet_list, name='list'),
    # path('<int:pk>/', views.snippet_detail, name='detail'),
    path('', views.snippet_list, name='list'),
    path('<int:pk>/', views.snippet_detail, name='detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)