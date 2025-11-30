from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import BlogPosts

class BlogPostView(ListView) :
    model = BlogPosts
    template_name = 'blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['object_list']
        return context 
    
class BlogDetailView(DeleteView) :
    model = BlogPosts
    template_name = "blogDetail.html"
    
    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context['post'] = context['object']
        return context

# Create your views here.
