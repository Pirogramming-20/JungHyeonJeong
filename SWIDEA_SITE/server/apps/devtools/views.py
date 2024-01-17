from django.shortcuts import render, redirect
from .models import Devtool
from .forms import DevtoolForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def devtools_list(request):
    devtools = Devtool.objects.all()
    ctx = {
        'devtools' : devtools,
    }
    return render(request, 'devtools/devtool_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = DevtoolForm()
        ctx = {
            'form' : form,
        }
        return render(request, 'devtools/devtool_create.html', ctx)
    form = DevtoolForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('devtools:list')

def detail(request, pk):
    devtool = Devtool.objects.get(id=pk)
    related_ideas = devtool.idea_set.all()
    ctx = {
        'devtool': devtool,
        'related_ideas' : related_ideas,
    }
    return render(request, 'devtools/devtool_detail.html', ctx)

def update(request, pk):
    devtool = Devtool.objects.get(id=pk)
    if request.method == 'GET':
        form = DevtoolForm(instance=devtool)
        ctx = {
            'form' : form,
            'pk' : pk,
        }
        return render(request, 'devtools/devtool_update.html', ctx)
    form = DevtoolForm(request.POST, instance=devtool)
    if form.is_valid():
        form.save()
    return redirect('devtools:detail', pk)

def delete(request, pk):
    if request.method == 'POST':
        Devtool.objects.get(id=pk).delete()
    return redirect('devtools:list')

@csrf_exempt
def search(request):
    search_txt = request.body.decode()

    devtools = Devtool.objects.all()
    if search_txt:
        devtools = devtools.filter(name__contains=search_txt)
    ctx = {
        'devtools' : devtools,
    }
    return render(request, 'devtools/devtool_list_part.html', ctx, content_type='text/plain')