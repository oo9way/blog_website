from django.shortcuts import render
from blog.models import Post, Category
from django.db.models import Q

# Create your views here.
def main_page(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    
    text = request.GET.get("search", None)
    category = request.GET.get("cat", None)
    
    if text:
        posts = posts.filter(Q(title__icontains=text) | Q(body__icontains=text))

    if category:
        posts = posts.filter(category_id=category)
    
    
    context = {
        "posts": posts,
        "categories": categories
    }
    return render(request, "main.html", context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)

    except Post.DoesNotExist:
        post = None
    
    
    context = {
        'post':post
    }
    return render(request, "detail.html", context)