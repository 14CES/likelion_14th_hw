from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()
    number = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def summary(self):
        return self.content[:20]
    
class Comment(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.post.title}: {self.content[:20]} by {self.writer.profile.nickname}"