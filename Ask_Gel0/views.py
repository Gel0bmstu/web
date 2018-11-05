from django.shortcuts import render
from django.utils import timezone
from .models import Post, Tag
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Новые вопросы
def post_list(request):
    posts = Post.objects.post_new()
    paginator = Paginator(posts, 4) # Show 4 contacts per page

    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    return render(request, 'Ask_Gel0/index.html', {'posts': page})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'Ask_Gel0/tag.html', {'tags': tags})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Ask_Gel0/question.html', {'post': post})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'Ask_Gel0/ask.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Ask_Gel0/ask.html', {'form': form})

def post_hot(request):
    posts = Post.objects.order_by('-likes')
    paginator = Paginator(posts, 4) # Show 4 contacts per page

    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    return render(request, 'Ask_Gel0/index.html', {'posts': page})

def login(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-lieks')
    return render(request, 'Ask_Gel0/login.html', {'posts' : posts})

def signup(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-lieks')
    return render(request, 'Ask_Gel0/signup.html', {'posts' : posts})

def post_tag(request, tag):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('tag')
    return render(request, 'Ask_Gel0/index.html', {'posts' : posts})

def settings(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-lieks')
    return render(request, 'Ask_Gel0/settings.html', {'posts' : posts})