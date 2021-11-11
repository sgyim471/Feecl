from django.urls import path
from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    path('', SubjectListView.as_view(),name='list'),
    path('detail/<int:pk>/', SubjectDetailView.as_view(),name='detail'),
    path('logout/',views.logout,name='logout'),
]