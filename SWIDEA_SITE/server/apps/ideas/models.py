from django.db import models
from apps.devtools.models import Devtool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=30)
    image = models.ImageField('Image', upload_to='ideas/%Y%m%d')
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', default=0)
    created_date = models.DateTimeField('등록일', auto_created=True, auto_now_add=True)
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name='예상 개발툴')
    ideaStar = models.BooleanField(default=False)

    def __str__(self):
        return self.title