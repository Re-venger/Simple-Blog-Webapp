from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User



class PostsListView(ListView):
    model = Posts
    template_name = 'blogs/index.html'
    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']   # this will order the posts in the defined way
    paginate_by = 5


class PostsDetailView(DetailView):
    model = Posts
    template_name = 'blogs/post_detail.html'



class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'blogs/post_form.html'

    fields = ['title', 'content']

    def form_valid(self, form):
        # set the current logged in user as the author
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    template_name = 'blogs/post_update.html'

    fields = ['title', 'content']

    def form_valid(self, form):
        # set the current logged in user as the author
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'
    template_name = 'blogs/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



class UserPostsListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'blogs/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by("-date_posted")
        

# def index(request):
#     context = {
#         'posts':Posts.objects.all().order_by('-date_posted')
#     }
#     return render(request, 'blogs/index.html', context)



def about(request):
    return render(request, 'blogs/about.html')