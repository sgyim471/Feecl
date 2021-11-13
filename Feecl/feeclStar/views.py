from django.shortcuts import render,redirect
from django.views.generic.list import ListView 
from .models import Subject,Comment
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.http.response import HttpResponse, HttpResponseRedirect


class SubjectListView(ListView):
    model = Subject

    
def detail(request,pk):
    subject = Subject.objects.get(pk=pk)
    comment = Comment.objects.filter(subject_id=subject)
    total = 0
    for i in comment:
        total += i.comment_star
    if total != 0:
        subject_star = total/len(comment)
        subject.subject_star = round(subject_star,2)
        subject.save()
    return render(request,'feeclStar/subject_detail.html',{'subject':subject,'comment':comment})

def create(request,pk):
    if request.method == "POST":
        comment_text = request.POST.get('comment_text',None)
        comment_star = request.POST.get('comment_star',None)
        subject_id = Subject.objects.get(id = pk)
        res_data={}
        if not(comment_star and comment_text):
            res_data['error'] = '모두 입력해주세요'
        else:
            write = Comment(comment_text=comment_text, comment_star=comment_star,subject_id = subject_id)
            write.save()
            return HttpResponseRedirect(reverse('detail',kwargs={'pk':pk}))



        return render(request,'feeclStar/subject_comment.html',res_data)
    
    else:
        return render(request,'feeclStar/subject_comment.html')

def logout(request):
    request.session.pop('user')
    return redirect('/main')