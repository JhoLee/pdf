from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, FormView

from .forms import PostForm
from .models import Post
from .utils import encrypt, check_pw


def index(req, **kwargs):
    return render(req, 'mask/index.html')


class IndexView(ListView):
    template_name = 'mask/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-reg_date')[:5]


class PostDetailView(View):
    def get(self, req, pk):
        context = {}
        try:
            post = Post.objects.get(pk=pk)
            context['post'] = post
            context['msg'] = "INFO: 이미지를 보려면, 암호를 입력하셔야 합니다."
        except Exception:
            context['msg'] = "WARN: The post was not found."
        return render(req, 'mask/check_password.html', context)

    def post(self, req, pk):
        context = {}

        try:
            if 'password' not in req.POST.keys():
                context['msg'] = "WARN: Error"

            input_pw = req.POST['password']
            post = Post.objects.get(pk=pk)
            context['post'] = post
            print(req.POST)
            hashed_pw = post.password
            print(input_pw)
            if check_pw(input_pw, hashed_pw):
                context['msg'] = "INFO: Password match!"
                print('check true')

                return render(req, 'mask/detail.html', context)
            else:
                print('check false')
                context['msg'] = "WARN: Password doesn't match"

                return render(req, 'mask/check_password.html', context)
        except Exception:
            print(Exception)
            context['msg'] = "WARN: The post was not found."
        return render(req, 'mask/check_password.html', context)


class _PostDetailView(DetailView):
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
            post.password = encrypt(post.password)
            post.save()
            pk = post.pk
            return redirect('mask:detail', pk=pk)


def delete_post(req, pk):
    context = {}
    try:
        post = Post.objects.get(pk=pk)
        post.delete()
        context['msg'] = "INFO: Deleted."
    except Exception:
        context['msg'] = "WARN: The post was not found."

    return redirect('mask:index')
