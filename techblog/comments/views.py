from django.shortcuts import render, redirect
from.forms import CommentForm
from.models import Comment
from blog.models import Blog
# Create your views here.

def add_comment(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'blog': blog})