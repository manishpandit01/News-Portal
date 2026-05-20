from django.urls import path
from newsportal import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
]
