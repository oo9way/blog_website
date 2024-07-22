from django.shortcuts import render
from blog.models import Post, Category, Resume, Message
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


def resume_page(request):
    resume = Resume.objects.filter(is_active=True).first()

    context = {
        "resume":resume
    }

    return render(request, "resume.html", context)


def message_page(request):
    errors = ""
    success = ""
    if request.method == "POST":
        phone = request.POST.get("phone", None)
        text = request.POST.get("text", None)

        if phone and text:
            Message.objects.create(phone=phone, text=text)
            success = "Sizning xabaringiz yuborildi"
        else:
            errors = "Phone and text are required"

    context = {
        "errors": errors,
        "success": success
    }
    return render(request, "message.html", context)