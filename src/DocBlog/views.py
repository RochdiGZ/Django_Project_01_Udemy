# Second code
from datetime import datetime
from django.shortcuts import render


def index(request):
    return render(request, "DocBlog/index.html", context={"prenom": "Patrick", "date": datetime.today()})


"""
# First code
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Bonjour, binevenue sur mon site</h1>")
"""