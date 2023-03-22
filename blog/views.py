from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Author, Tag
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm

# Create your views here.


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']  # desc -> from the oldest to the latest.
    # by default django uses object_list or post_list name in templates but we can edit it
    context_object_name = 'posts'

    # to limit shown posts to 3
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# starting_page -> index.html page
# def starting_page(request):
#     # this gets all posts and ordered it descending by date and show only 3
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/index.html', {
#         'posts': latest_posts
#     })

class AllPostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#     return render(request, 'blog/all-posts.html', {
#         'all_posts': all_posts
#     })


class SinglePostView(View):
    # template_name = 'blog/post-detail.html'
    # model = Post
    # and it automatically know the post by slug that i use in url

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': CommentForm,
            'comments': post.comments.all().order_by('-id')

        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post #here i'm sure that this comment added to this post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        
        context = {
            'post': post,
            'post_tags': post.tags.all(),
            'comment_form': comment_form,
            'comments': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/post-detail.html', context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # access all the tags for this given post
    #     context['post_tags'] = self.object.tags.all()
    #     # created a new form and pass it to context that will render it in post-detail
    #     context['comment_form'] = CommentForm()
    #     return context


# def post_detail(request, slug):
#     # identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-detail.html', {
#         'post': identified_post,
#         'post_tags': identified_post.tags.all(),
#     })
