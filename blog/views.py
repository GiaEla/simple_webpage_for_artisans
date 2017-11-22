from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from blog.models import Post, Category


def show_post(request, pk):

    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post.html', {'post': post})


def all_posts(request):

    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.POSTS_PER_PAGE)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    page_numbers = [i + 1 for i in range(posts.paginator.count)]

    return render(request, 'blog/all_posts.html', {'posts': posts, 'page_numbers': page_numbers})


def all_categories(request):

    categories = Category.objects.all()

    return render(request, 'blog/all_categories.html', {'categories': categories})


def show_category(request, pk):

    category = Category.objects.get(pk=pk)
    post_list = Post.objects.filter(category=category)
    paginator = Paginator(post_list, settings.POSTS_PER_PAGE)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    page_numbers = [i+1 for i in range(posts.paginator.count)]

    return render(request, 'blog/category.html', {'category': category, 'posts': posts, 'page_numbers': page_numbers})


def search(request):
    words = request.GET.get('q')
    if words:
        post_list = Post.objects.filter(
            Q(title__icontains=words) |
            Q(sub_title__icontains=words) |
            Q(lead__icontains=words) |
            Q(content__icontains=words)
        )

        queries = words.split()

        if queries[0] != words:
            for query in queries:
                new_list = Post.objects.filter(
                    Q(title__icontains=query) |
                    Q(sub_title__icontains=query) |
                    Q(lead__icontains=query) |
                    Q(content__icontains=query)
                )

                post_list_tags = Post.objects.filter(
                    tags__contains=[query]
                )

                post_list = post_list.union(new_list, post_list_tags)
    else:
        post_list = []

    return render(request, 'blog/search.html', {'posts': post_list})


