from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.
def main(request):
    posts = Post.objects.all()
    ctx = {
        'posts' : posts,
    }
    return render(request, 'posts/post_main.html', ctx)

def create(request):
    if request.method == 'GET':
        form = PostForm()
        ctx = {
            'form' : form,
        }
        return render(request, 'posts/post_create.html', ctx)
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('posts:main')

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    post_id = req['id']
    post = Post.objects.get(id=post_id)

    if post.like == False:
        post.like = True
    else:
        post.like = False
    
    post.save()

    return JsonResponse({'id' : post_id, 'type' : post.like})

@csrf_exempt
def create_comment(request):
    req = json.loads(request.body)
    post_id = req['id']
    comment_content = req['comment']

    post = Post.objects.get(id=post_id)
    newComment = Comment.objects.create(post_id=post, content=comment_content)
    return JsonResponse({'post_id' : post_id, 'comment_id' : newComment.id, 'content' : comment_content})

@csrf_exempt
def delete_comment(request):
    req = json.loads(request.body)
    post_id = req['post_id']
    comment_id = req['comment_id']

    Comment.objects.get(id=comment_id).delete()
    return JsonResponse({'post_id' : post_id, 'comment_id' : comment_id})