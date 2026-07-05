from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost
from .forms import BlogCommentForm

# Create your views here.


def blog(request):
    """ To show all of the blogposts in a grid """
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'showrunners/blog.html', context)


def blog_detail(request, slug):
    """ Shows an individual blog post in full detail including any comments """
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.all()
    
    if request.method == 'POST':

        if not request.user.is_authenticated:
            messages.error(request, "Access Denied. You must be logged in to leave commentary.")
            return redirect('account_login')
            
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user 
            comment.save()
            messages.success(request, "Comment Posted! Welcome to the party.")
            return redirect('blog_detail', slug=post.slug)
    else:
        form = BlogCommentForm()
        
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'showrunners/blog_detail.html', context)