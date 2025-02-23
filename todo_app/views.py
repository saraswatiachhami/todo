from django.shortcuts import render

# Create your views here.

from todo_app.models import Todo
from django.http import HttpResponseRedirect

def todo_list(request):
    todos = Todo.objects.all()
    return render (
        request,
        "bootstrap/todo_list.html",
        {"todos":todos},
    )


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")


def todo_create(request):
    if request.method == "GET":
        return render(
        request,
        "bootstrap/todo_create.html",

        )
    else:
        todo = Todo(title=request.POST["title"])
        todo.save()
        return HttpResponseRedirect("/")

    
def todo_update(request, id):
    if request.method == "GET":
        todo = Todo.objects.get(id=id)
        return render(
            request,
            "bootstrap/todo_update.html",
            {"todo": todo},
        )
    else:
        todo = Todo.objects.get(id=id)
        todo.title = request.POST['title']
        todo.save()
        return HttpResponseRedirect("/")