from django.urls import path
from . import views

urlpatterns = [
    path("", views.home), # URL for the home view
    path("logout", views.logout_view), #URL for the logout view
]