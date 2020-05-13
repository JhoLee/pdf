from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, FormView

from .forms import PostForm
from .models import Post


def index(req):
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
        return render(request, 'mask/request.html', {'form': form})

    def post(self, request, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #

            post.save()
            pk = post.pk
            return redirect('mask:detail', pk=pk)
