from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, FormView

from .forms import PostForm
from .models import Post


def index(req, **kwargs):
    return render(req, 'mask/index.html')


class IndexView(ListView):
    template_name = 'mask/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-reg_date')[:5]


class PostDetailView(DetailView):
    model = Post
    template_name = 'mask/detail.html'


class PostFormView(FormView):
    def get(self, request, **kwargs):
        form = PostForm()
        context = {'form': form}
        return render(request, 'mask/post.html', context=context)

    def post(self, request, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #

            post.save()
            pk = post.pk
            return redirect('mask:detail', pk=pk)


def delete_post(req, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.delete()
        msg = "INFO: Deleted."
    except Exception:
        msg = "WARN: The post was not found."

    context = {
        'alert': msg
    }
    return redirect('mask:index')
