from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import ToDoItem

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  todo_items = ToDoItem.objects.order_by("-id").all()
  return render(
    request, 
    "todo_list/index.html",
    context={"todo_items": todo_items}
  )