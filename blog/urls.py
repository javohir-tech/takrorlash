from django.urls import path
from .views import (
    BlogPostView,
    BlogDetailView,
    CreateBlogView,
    UpdateBlogView,
    DeleteBlogView
    )

urlpatterns = [
    path('', BlogPostView.as_view(), name="blog"),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name="blog_detail" ),
    path('blog/create' , CreateBlogView.as_view(), name="createblog"),
    path('blog/edit/<int:pk>/', UpdateBlogView.as_view() , name="blog_edit"),
    path('blog/delete/<int:pk>', DeleteBlogView.as_view(), name='blog_delete')
]