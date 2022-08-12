# from django.contrib import messages
# from django.shortcuts import (
#     render,
#     get_object_or_404,
#     redirect,
# )
# from django.utils.decorators import method_decorator
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView,
# )
# from .forms import PostModelForm, CommentModelForm
# from .models import Category, Post, Comment
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy, reverse
# from django.views.decorators.cache import cache_page
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.utils.text import slugify
# from transliterate import translit
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
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


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 5
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        print(data)
        return data


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
        return reverse('detail_post', kwargs={'slug': self.object.slug, 'category': category})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    extra_context = {
        'comments_form': CommentModelForm()
    }

# @login_required()
# def new_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST or None, files=request.FILES or None)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('index')
#         else:
#             return render(request, 'new.html', {'form': form})
#     else:
#         form = PostForm()
#     return render(request, 'new.html',
#                   {'form': form,
#                    'button_name': 'Добавить',
#                    'title': 'Добавить запись',
#                    'url_name': 'new_post'}
#                   )

# @login_required()
# class NewPost(CreateView):
#     form_class = BookForm
#     success_url = reverse_lazy("index")
#     template_name = "test.html"
#
#     def form_valid(self, form):
#         return super().form_valid(form)