from django.shortcuts import render

# Create your views here.
def home(request):
      return render(request, 'webcv/home.html')

def about(request):
      return render(request, 'webcv/about.html')

def contact(request):
      return render(request, 'webcv/contact.html')

def projects(request):
      return render(request, 'webcv/projects.html')

