# Second code
from django.shortcuts import render


def blog_index(request):
    return render(request, "blog/index.html")


def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{numero_article}.html", context={})
    return render(request, "blog/article_not_found.html")


"""
# First code
from django.http import HttpResponse


def blog_index(request):
    return HttpResponse("<h1>Bonjour, binevenue sur mon site</h1>")
"""