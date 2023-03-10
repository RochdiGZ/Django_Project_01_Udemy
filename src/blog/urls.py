from django.urls import path
from .views import blog_index, article

urlpatterns = [
    path('', blog_index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article"),
]
