from django.shortcuts import render
from .models import Article
# Create your views here.
def Home(request):
    posts=Article.objects.all()
    return render(request,'home.html',{'posts':posts})