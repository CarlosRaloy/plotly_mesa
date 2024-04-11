from . import views
from django.urls import path

urlpatterns = [
    path('',views.plot,name='plots'),
]