from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItems
# Create your views here.


def index(request):
    all_entries = TodoItems.objects.all()
    return render(request, "index.html", {'items': all_entries})


def add(request, item):
    TodoItems.objects.create(item=item)
    return redirect("/")


def dlt(request, itemId):
    TodoItems.objects.filter(id=itemId).delete()
    return redirect("/")
