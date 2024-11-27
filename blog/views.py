from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_index(request):
    posts_list = Post.objects.all().order_by('-created_on')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 20)
    page_obj = paginator.get_page(page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def blog_category(request, category):
    posts_list = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 20)
    page_obj = paginator.get_page(page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'blog/category.html', context)


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': CommentForm(),
    }
    return render(request, 'blog/detail.html', context)