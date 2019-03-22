from django.shortcuts import render
from newSite.models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'website/post_list.html', {'posts':posts})