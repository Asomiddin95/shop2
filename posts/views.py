from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from posts.models import PostModel
from posts.forms import CommentFormModel
from django.urls import reverse
from django.shortcuts import get_object_or_404
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


class CommentCreateView(CreateView):
    form_class = CommentFormModel

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.kwargs.get('pk')})
