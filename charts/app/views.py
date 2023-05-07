from django.shortcuts import render
from .models import Vote


def index(request):
    votes = Vote.objects.all()

    context = {"votes": votes}
    return render(request, "index.html", context)
