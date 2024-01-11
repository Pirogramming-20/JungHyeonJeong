from django.db import models

# Create your models here.

# 영화 제목, 개봉 년도, 장르, 별점 / 감독, 주연, 러닝타임, 리뷰 내용
class Review(models.Model):
    title = models.CharField(max_length=30)
    releaseDate = models.DateField()
    genre = models.CharField(max_length=10)
    rating = models.FloatField()
    director = models.CharField(max_length=30)
    actors = models.TextField()
    time = models.IntegerField()
    content = models.TextField()