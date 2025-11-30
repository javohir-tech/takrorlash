from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPosts

class BlogPostView(ListView) :
    model = BlogPosts
    template_name = 'blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['object_list']
        return context 

# Create your views here.
