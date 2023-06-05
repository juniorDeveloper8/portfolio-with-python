from django.shortcuts import render, get_object_or_404
from blog.models import Posts

def article(request):

    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, posts_id):
    token = get_object_or_404(Posts, pk=posts_id)
    return render(request, 'details.html', {'token': token })