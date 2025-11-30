from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
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
    
class CreateBlogView(CreateView):
    model = BlogPosts;
    template_name = "createblog.html"
    fields = ['title' , 'text' , 'author']
    
class UpdateBlogView(UpdateView) :
    model = BlogPosts;
    template_name = 'editblog.html'
    fields = ['title' , 'text']


class DeleteBlogView(DeleteView) :
    model = BlogPosts;
    template_name = 'deleteBlog.html'
    success_url = reverse_lazy('blog')

