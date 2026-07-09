from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BlogPost
from .forms import BlogCommentForm
from django.db.models import Q

# Create your views here.


def blog(request):
    """ To show all of the blogposts in a grid & search bar"""
    posts = BlogPost.objects.all()

    query = request.GET.get('q')
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))   # noqa: E501

    context = {
        'posts': posts,
        'search_query': query,
    }
    return render(request, 'showrunners/blog.html', context)


def blog_detail(request, slug):
    """ Shows an individual blog post in full detail including any comments """
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':

        if not request.user.is_authenticated:
            messages.error(request, "Access Denied. You must be logged in to comment.")   # noqa: E501
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
