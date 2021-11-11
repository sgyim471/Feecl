from django.shortcuts import render,redirect
from django.views.generic.list import ListView 
from .models import Subject
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

class SubjectListView(ListView):
    model = Subject

class SubjectDetailView(DetailView):
    model = Subject

def logout(request):
    request.session.pop('user')
    return redirect('/main')