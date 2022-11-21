from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status=1).exclude(
        published_date__gt=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request):
    return render(request, 'blog/blog-single.html')


def test(request, pid):

    post = get_object_or_404(Post, pk=pid)
    # next two lines are the answer of second question
    post.counted_view += 1
    post.save()
    context = {'post': post}
    return render(request, 'test.html', context)
