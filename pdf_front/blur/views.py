from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic

from .models import Request


def index(req):
    return render(req, 'blur/index.html')


class IndexView(generic.ListView):
    template_name = 'blur/index.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return Request.objects.order_by('-reg_date')[:5]


class DetailView(generic.DetailView):
    model = Request
    template_name = 'blur/index.html'

