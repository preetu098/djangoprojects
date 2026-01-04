from django.shortcuts import render,redirect
from .models import Post
# Create your views here.

def add_post(request):
    if(request.method=='POST'):
        title=request.POST['title']
        content=request.POST['content']
        Post.objects.create(title=title,content=content)
        return redirect('add_page')
    return render(request,'add_post.html')

def all_post(request):
    post=Post.objects.all()
    return render(request,'all_post.html',{'post':post})


