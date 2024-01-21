from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='ideas/%Y%m%d')
    content = models.TextField()
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content