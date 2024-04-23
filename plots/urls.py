from . import views
from django.urls import path

urlpatterns = [
    path('',views.Plot1DView.as_view(),name='plots'),
    path('avg/', views.Plot2DView.as_view(),name='avg'),
]