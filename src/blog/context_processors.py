from blog.models import Post

from django.shortcuts import render

def select_list_data(request):
    """
    Adds data needed by select list to every template via context processor.
    """

    return {
        'posts': Post.objects.all().order_by('title'),
        'categories': (i['tags'] for i in Post.objects.values('tags').distinct()),
    }