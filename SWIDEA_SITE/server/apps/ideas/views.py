from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm

# Create your views here.
def main(request):
    ideas = Idea.objects.all()
    orderCondition = request.GET.get('orderBy')

    if orderCondition == "이름순":
        ideas = Idea.objects.order_by('title')
    elif orderCondition == "등록순":
        ideas = Idea.objects.order_by('created_date')
    elif orderCondition == "최신순":
        ideas = Idea.objects.order_by('-updated_date')
    else:
        ideas = Idea.objects.order_by('title')
    
    ctx = {
        'ideas' : ideas,
        'orderCondition' : orderCondition,
    }
    return render(request, 'ideas/idea_list.html', ctx)

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
