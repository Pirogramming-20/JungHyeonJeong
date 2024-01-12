from django.db import models

# Create your models here.

# 영화 제목, 개봉 년도, 장르, 별점 / 감독, 주연, 러닝타임, 리뷰 내용
class Review(models.Model):
    genreChoices = [
        ('액션', '액션'),
        ('범죄', '범죄'),
        ('SF', 'SF'),
        ('코미디', '코미디'),
        ('공포', '공포'),
        ('전쟁', '전쟁'),
        ('애니메이션', '애니메이션'),
        ('드라마', '드라마'),
        ('로맨스', '로맨스'),
    ]

    title = models.CharField(max_length=30)
    releaseDate = models.DateField()
    genre = models.CharField(max_length=10, choices=genreChoices, default='액션')
    rating = models.FloatField()
    director = models.CharField(max_length=30)
    actors = models.TextField()
    time = models.IntegerField()
    content = models.TextField()