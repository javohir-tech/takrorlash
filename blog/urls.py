from django.urls import path
from .views import BlogPostView, BlogDetailView

urlpatterns = [
    path('', BlogPostView.as_view(), name="blog"),
    path('blogs/<int:pk>/', BlogDetailView.as_view(),name="blog_detail" )
]