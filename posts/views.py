from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import PostModel


# Create your views here.


class PostListView(ListView):
    template_name = 'blog.html'
    paginate_by = 3

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        if qs:
            qs = qs.filter(tags__title=tag)
        return qs


class PostDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
