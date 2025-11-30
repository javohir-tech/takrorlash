from django.db import models

class BlogPosts(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


# Create your models here.
