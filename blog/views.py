
from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    query = request.GET.get("q", "")

    posts = Post.objects.filter(published_at=True)

    if query:
        posts = posts.filter(title__icontains=query) | Post.objects.filter(
            published_at=True,
            content__icontains=query
        )

    posts = posts.order_by("-created_at")

    return render(
        request,
        "blog/home.html",
        {"posts": posts, "query": query}
    )


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        published_at=True
    )
    return render(request, "blog/post_detail.html", {"post": post})
