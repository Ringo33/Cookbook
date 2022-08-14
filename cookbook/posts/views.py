from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from transliterate import translit
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from .models import Category, Post, Comment
from .forms import PostModelForm, CommentModelForm


# @method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 8
    context_object_name = 'posts'
    extra_context = {
        'category': Category.objects.all(),
        'status': 'active'
    }

    def get_queryset(self):
        request = self.request.GET.get('s', '')
        name = slugify(translit(request, language_code='ru', reversed=True))
        object_list = Post.objects.filter(slug__icontains=name)
        return object_list


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    paginate_by = 8
    context_object_name = 'posts'
    extra_context = {
        'category': Category.objects.all()
    }

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('category'))
        request = self.request.GET.get('s', '')
        name = slugify(translit(request, language_code='ru', reversed=True))
        if name:
            object_list = Post.objects.filter(slug__icontains=name)
        else:
            object_list = category.posts.all()
        return object_list

    # добавление в контекст категории, чтобы транслировать в categories_list.html
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['status'] = self.kwargs.get('category')
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'posts_add.html'

    def form_valid(self, form):
        posts = form.save(commit=False)
        posts.author = self.request.user
        posts.slug = slugify(translit(posts.title, language_code='ru', reversed=True))
        posts.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Пост "{posts.title}" добавлен',
            extra_tags='success'
        )
        return super().form_valid(form)

    def get_success_url(self):
        category = slugify(translit(str(self.object.category), language_code='ru', reversed=True))
        # return reverse('detail_post', kwargs={'slug': self.object.slug, 'category': self.object.category.slug})
        return reverse('detail_post', kwargs={'slug': self.object.slug, 'category': category})


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    extra_context = {
        'comments_form': CommentModelForm()
    }


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        posts = form.save(commit=False)
        posts.author = self.request.user
        posts.slug = slugify(translit(posts.title, language_code='ru', reversed=True))
        posts.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Пост "{posts.title}" добавлен',
            extra_tags='success'
        )
        return super().form_valid(form)

    @property
    def success_url(self):
        category = slugify(translit(str(self.object.category), language_code='ru', reversed=True))
        return reverse('detail_post', kwargs={'slug': self.object.slug, 'category': category})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        messages.add_message(
            self.request, messages.INFO, f'Пост {self.object.title} удален', extra_tags='info'
        )
        return super().get_context_data(**kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentModelForm

    def form_valid(self, form):
        comments = form.save(commit=False)
        comments.author = self.request.user
        comments.post = Post.objects.get(slug=self.kwargs.get('slug'))
        comments.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_post', kwargs={'slug': self.kwargs.get('slug'), 'category': self.kwargs.get('category')})
