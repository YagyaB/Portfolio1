from django.shortcuts import render

# Create your views here.
def index(request):
      return render(request, 'webcv/index.html')

def post(request):
      return render(request, 'webcv/post.html')

def contact(request):
      return render(request, 'webcv/contact.html')

def projects(request,pk):
      return render(request, 'webcv/contact.html')