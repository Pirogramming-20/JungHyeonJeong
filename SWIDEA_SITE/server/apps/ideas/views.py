from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Idea
from .forms import IdeaForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    ideas = Idea.objects.all()
    orderCondition = request.GET.get('orderBy')

    if orderCondition == "이름순":
        ideas = Idea.objects.order_by('title')
    elif orderCondition == "등록순":
        ideas = Idea.objects.order_by('created_date')
    elif orderCondition == "최신순":
        ideas = Idea.objects.order_by('-created_date')
    elif orderCondition == "찜하기순":
        ideas = Idea.objects.order_by('-ideaStar', 'title')
    else:
        ideas = Idea.objects.order_by('title')
    
    ctx = {
        'ideas' : ideas,
        'orderCondition' : orderCondition,
    }
    return render(request, 'ideas/idea_list.html', ctx)

@csrf_exempt
def star(request, pk):
    idea = Idea.objects.get(id=pk)
    if idea.ideaStar == False:
        idea.ideaStar = True
    elif idea.ideaStar == True:
        idea.ideaStar = False
    idea.save()
    return HttpResponse(str(idea.ideaStar))


def create(request):
    if request.method == 'GET':
        form = IdeaForm()
        ctx = {
            'form' : form,
        }
        return render(request, 'ideas/idea_create.html', ctx)
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('ideas:main')

def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    devtool = idea.devtool
    ctx = {
        'idea' : idea,
        'devtool' : devtool,
    }
    return render(request, 'ideas/idea_detail.html', ctx)

def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        ctx = {
            'form' : form,
            'pk' : pk,
        }
        return render(request, 'ideas/idea_update.html', ctx)
    form = IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
    return redirect('ideas:detail', pk)


def delete(request, pk):
    if request.method == 'POST':
        Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')

@csrf_exempt
def count(request, pk):
    if request.method == 'POST':
        btn_type = request.body.decode()
        idea = Idea.objects.get(id=pk)

        if btn_type == 'plus':
            idea.interest += 1
        elif btn_type == 'minus':
            idea.interest -= 1
        idea.save()

        return HttpResponse(str(idea.interest))
