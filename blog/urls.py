from django.urls import path
from .views import BlogPostView, BlogDetailView, CreateBlogView

urlpatterns = [
    path('', BlogPostView.as_view(), name="blog"),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name="blog_detail" ),
    path('blog/create' , CreateBlogView.as_view(), name="createblog")
]