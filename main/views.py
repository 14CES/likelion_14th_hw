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
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request,'main/new_post.html')

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    new_post = Post()

    new_post.title=request.POST['title']
    new_post.writer=request.user
    new_post.pub_date=request.POST['pub_date']
    new_post.content=request.POST['content']
    new_post.number=request.POST['number']

    new_post.save()

    save_tags(new_post)

    return redirect('main:detail', new_post.id)

def postpage(request):
    posts=Post.objects.all()
    return render(request,'main/postpage.html',{'posts':posts})

def edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    edit_post = get_object_or_404(Post, pk=post_id)

    if edit_post.writer != request.user:
        return redirect('main:detail', edit_post.id)
    
    return render(request, 'main/edit.html',{"post": edit_post})

def edit_comment(request, comment_id): 
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    edit_comment=get_object_or_404(Comment, pk=comment_id)
    
    if edit_comment.writer != request.user:
        return redirect('main:detail', edit_comment.post.id)

    return render(request, 'main/edit_comment.html',{"comment": edit_comment})


def update(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    update_post = get_object_or_404(Post, pk=post_id)
    
    if update_post.writer != request.user:
        return redirect('main:detail', update_post.id)
    
    update_post.title = request.POST['title']
    update_post.writer= request.user
    update_post.pub_date= request.POST['pub_date']
    update_post.content= request.POST['content']
    update_post.number= request.POST.get('number', 0)
    
    update_post.save()

    save_tags(update_post)

    return redirect('main:detail', update_post.id)


def update_comment(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    update_comment=get_object_or_404(Comment, pk=comment_id)

    if update_comment.writer != request.user:
        return redirect('main:detail', update_comment.post.id)

    update_comment.writer= request.user
    update_comment.pub_date= request.POST['pub_date']
    update_comment.content= request.POST['content']

    update_comment.save()

    return redirect('main:detail', update_comment.post.id)

def delete(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    delete_post=get_object_or_404(Post, pk=post_id)
    
    if delete_post.writer != request.user:
        return redirect('main:detail', delete_post.id)
    
    delete_post.delete()

    return redirect('main:postpage')

def delete_comment(request, comment_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    delete_comments=get_object_or_404(Comment, pk=comment_id)
    
    if delete_comments.writer != request.user:
        return redirect('main:detail', delete_comments.post.id)
    
    delete_comments.delete()

    return redirect('main:detail', delete_comments.post.id)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST' and request.user.is_authenticated:
        new_comments = Comment()

        new_comments.post = post
        new_comments.writer = request.user
        new_comments.content = request.POST['content']

        new_comments.save()
        return redirect('main:detail', post_id)
    
    comments = Comment.objects.filter (post=post)
    return render(request, 'main/detail.html',{'post':post, 'comments':comments})

def save_tags(post):
    words = post.content.split()
    tag_list = []
    for w in words:
        if len(w) > 0:
            if w[0] == '#':
                tag_list.append(w[1:])

    post.tags.clear()

    for t in tag_list:
        tag, boolean = Tag.objects.get_or_create(name=t)
        post.tags.add(tag)


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag_list.html',{'tags': tags})

def tag_post_list(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag_post_list.html', {'tag': tag, 'posts':posts})

def likes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()

    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()

    return redirect('main:detail', post.id)

def comment_likes(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user in comment.comment_like.all():
        comment.comment_like.remove(request.user)
        comment.comment_like_count -= 1
        comment.save()

    else:
        comment.comment_like.add(request.user)
        comment.comment_like_count += 1
        comment.save()

    return redirect('main:detail', comment.post.id)