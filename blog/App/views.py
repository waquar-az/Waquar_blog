from django.shortcuts import render,get_object_or_404
from .models import Article
# Create your views here.
def Home(request):
    posts=Article.objects.all()
    return render(request,'home.html',{'posts':posts})

def Detail(request,pk):
    post=get_object_or_404(Article,pk=pk)
    return render(request,'detail_page.html',{'post':post})

def About(request):
    return render(request,'about.html')