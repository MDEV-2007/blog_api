from django.db import models
from accounts.models import User
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/image/')
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']


    def __str__(self):
        return self.title

    