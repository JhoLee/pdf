from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, FormView

from .forms import RequestForm
from .models import Request


def index(req):
    return render(req, 'mask/index.html')


class IndexView(ListView):
    template_name = 'mask/index.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return Request.objects.order_by('-reg_date')[:5]


class RequestDetailView(DetailView):
    model = Request
    template_name = 'mask/index.html'


class RequestFormView(FormView):
    def get(self, request, **kwargs):
        form = RequestForm()
        return render(request, 'mask/request.html', {'form': form})


class _RequestFormView(FormView):
    form_class = RequestForm
    template_name = 'mask/request.html'
    success_url = '/'

    def form_valid(self, form):
        return super(RequestFormView, self).form_valid(form)
