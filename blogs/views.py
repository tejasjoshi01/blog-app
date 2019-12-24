from django.shortcuts import render, redirect
from .models import Blog
from .form import WriteBlogForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def writeBlog(request):
    if request.method == "POST":
        form = WriteBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            # blog.time = request.timezone.now()
            blog.save()
            print('saved')
            return redirect('home')

    else:
        form = WriteBlogForm()
    return render(request, 'blogs/write.html', {'form': form})



@login_required(login_url='/accounts/login/')
def allBlogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/allBlogs.html', {'blogs': blogs})

