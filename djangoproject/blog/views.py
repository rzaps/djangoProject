from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def new_post(request):
    error = None
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('blog')
        else:
            errors = "Ошибка заполнения"

    form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})