from . import views
from django.urls import path

urlpatterns = [
    path('',views.Plot1DView.as_view(),name='plots'),
    path('avg/', views.Plot2DView.as_view(),name='avg'),
    path('improve/', views.Plot3DView.as_view(),name='improve'),
    path('dashed/', views.Plot4DView.as_view(),name='dash'),
    path('company/', views.Plot5DView.as_view(), name='company'),
]