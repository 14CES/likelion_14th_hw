from django.shortcuts import render, redirect, get_object_or_404
from .models import*

# Create your views here.

def mainpage(request): 
    return render(request, 'main/mainpage.html')

def secondpage(request):
    context={
        'generation': 14,
        'info':{
            'name' : '최은서',
            'age' : '2006년 04월 12일',
            'number' : '010-9158-3643'
        }
    }
    return render(request, 'main/secondpage.html', context)

def new_post(request):
    return render(request,'main/new_post.html')

def create(request):
    new_post = Post()

    new_post.title=request.POST['title']
    new_post.writer=request.POST['writer']
    new_post.pub_date=request.POST['pub_date']
    new_post.content=request.POST['content']
    new_post.number=request.POST['number']

    new_post.save()

    return redirect('main:detail', new_post.id)

def postpage(request):
    posts=Post.objects.all()
    return render(request,'main/postpage.html',{'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'main/detail.html', {'post':post})

def edit(request, post_id):
    edit_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/edit.html',{"post": edit_post})

def update(request, post_id):
    update_post = get_object_or_404(Post, pk=post_id)
    update_post.title = request.POST['title']
    update_post.writer= request.POST['writer']
    update_post.pub_date= request.POST['pub_date']
    update_post.content= request.POST['content']
    update_post.number= request.POST.get('number', 0)
    update_post.save()

    return redirect('main:detail', update_post.id)

def delete(request, post_id):
    delete_post=get_object_or_404(Post, pk=post_id)
    delete_post.delete()

    return redirect('main:postpage')