from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('items/', views.get_items),
    path('post-item/', views.post_item),
    path('request-item/', views.request_item),
]
