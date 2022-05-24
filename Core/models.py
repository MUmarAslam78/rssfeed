from django.db import models
from django.contrib.auth.models import User

# Create your models here .
class Blog(models.Model):
    
    STATUS = (
        (0, 'zero'),
        (1, 'one'),
        (2, 'two'),
    )
    blog_title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug":str(self.slug)})

class Document(models.Model):
    title = models.CharField(max_length = 200)
    upFile = models.CharField(max_length = 500,default="")
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

