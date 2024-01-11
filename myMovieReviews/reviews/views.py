from django.shortcuts import render, redirect
from .models import *

# Create your views here.

# 리뷰 리스트 : 영화 제목, 개봉 년도, 장르, 별점
def reviews_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews,
    }
    return render(request, 'reviews_list.html', context)


# 리뷰 디테일 : 영화 제목, 개봉 년도, 감독, 주연, 장르, 별점, 러닝타임, 리뷰 내용
def reviews_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        "review" : review,
    }
    return render(request, 'reviews_detail.html', context)


# 리뷰 작성하기
def reviews_create(request):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST['title'],
            releaseDate = request.POST['releaseDate'],
            genre = request.POST['genre'],
            rating = request.POST['rating'],
            director = request.POST['director'],
            actors = request.POST['actors'],
            time = request.POST['time'],
            content = request.POST['content'],
        )
        return redirect('/reviews')
    return render(request, 'reviews_create.html')
