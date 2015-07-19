from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from blog.models import Post

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

def individual_post(request, slug):
    """
    Returns an individual blog post, identified by its slug. If the get() 
    method raises a DoesNotExist exception, we render the postnotfound template.
    """

    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return render(request, 'notfound.html', {'search': 'post'})

    try:
        prev_post = post.get_previous_by_date()
    except Post.DoesNotExist:
        prev_post = None

    try:
        next_post =  post.get_next_by_date()
    except Post.DoesNotExist:
        next_post = None

    data = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'absolute_url': request.build_absolute_uri(post.get_absolute_url())
    }

    return render(request, 'singlepost.html', data)

def latest_posts(request):
    """
    Returns all blog posts ordered by date with pagnation if necessary. 
    """

    posts = Post.objects.all().order_by('-date')
    
    # Selects number of post objects to show per page 
    paginator = Paginator(posts, 8)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        blog_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        blog_list = paginator.page(paginator.num_pages)

    page_range = range(1, paginator.num_pages + 1)

    data = {
            'blog_list': blog_list,
            'latest_posts': True,
            'page_range': page_range
           }

    return render(request, 'blog.html', data)

def category_posts(request, category):
    """
    Returns all blog posts with a specified category value. If no 
    blog posts have this value, we render a user friendly error page. 
    """

    posts = Post.objects.filter(tags=category.title()).order_by('-date')
    
    if posts:
        data = {
            'topic': category,
            'blog_list': posts,
        }
        return render(request, 'blog.html', data)
    else:
        return render(request, 'notfound.html', {'search': 'category'})