from django.urls import path
from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    path('', SubjectListView.as_view(),name='list'),
    path('detail/<int:pk>/', detail,name='detail'),
    path('create/<int:pk>', create,name='create'),
    path('logout/',views.logout,name='logout'),
]

