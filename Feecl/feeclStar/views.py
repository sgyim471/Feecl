from django.shortcuts import render,redirect
from django.views.generic.list import ListView 
from .models import Subject,Comment
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

class SubjectListView(ListView):
    model = Subject

def detail(request,pk):
    subject = Subject.objects.get(pk=pk)
    comment = Comment.objects.get(subject_id= pk)
    return render(request,'feeclStar/subject_detail.html',{'subject':subject,'comment':comment})

def logout(request):
    request.session.pop('user')
    return redirect('/main')