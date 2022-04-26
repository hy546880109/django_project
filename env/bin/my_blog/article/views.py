from django.shortcuts import render
from django.http import HttpResponse

from .models import AriticlePost
# Create your views here.

def article_list(request):
    articles = AriticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)