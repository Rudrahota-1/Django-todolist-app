# todo/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem  # Ensure you have a model named TodoItem

def index(request):
    items = TodoItem.objects.all()  # Example: Fetch all items
    return render(request, 'index.html', {'items': items})

def remove(request, item_id):
    try:
        item_to_delete = TodoItem.objects.get(id=item_id)
        item_to_delete.delete()
        return redirect('todo')
    except TodoItem.DoesNotExist:
        return HttpResponse("Item not found", status=404)
