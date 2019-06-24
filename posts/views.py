from django.shortcuts import render
from .models import  Post
# from django.contrib.auth import User
# Create your views here.

def new_user(request):
	post = Post.objects.all()

	return render(request, 'new_user.html',{'post':post})
