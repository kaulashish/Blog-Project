from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post  #.models for current dir

# Create a fxn 'home' that handles the traffic from the home page of our blog

# def home(request):    #fxn based view
#     context = {'posts': Post.objects.all()}
#     # return rendered template instead of using httpresponse
#     # 1st arg is request obj, 2nd is template name
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):  #class based view for homepage
    model = Post
    template_name = 'blog/home.html'  # <appname>/<model>_<viewtype>.html
    context_object_name = 'posts'  #by default searches for context name as 'objectlist'
    ordering = ['-date_posted']  #'-' sign orders in reverse order


class PostDetailView(DetailView):
    model = Post
    #creating a post_detail.html template in /blog according to convention shown above to reduce code.


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'post']

    #overiding form_valid method to tell that the form is submitted by the user that signed in and not NULL.
    def form_valid(self, form):  #for IntegrityError
        form.instance.author = self.request.user  # i.e it takes the instance and sets the author equal to the logged in user.
        #run form_valid() on parent class after setting the author
        return super().form_valid(form)


#userpassestest mxin is used in order for the logged in to only update his own posts (order of inheritance matters!)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'post']

    #overiding form_valid method to tell that the form is submitted by the user that signed in and not NULL.
    def form_valid(self, form):  #for IntegrityError
        form.instance.author = self.request.user  # i.e it takes the instance and sets the author equal to the logged in user.
        #run form_valid() on parent class after setting the author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    #creating a post_detail.html template in /blog according to convention shown above to reduce code.

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
