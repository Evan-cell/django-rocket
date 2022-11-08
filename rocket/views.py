from django.shortcuts import render


# Create your views here.
def rocket(request):
    context = {}
    return render(request, 'blog.html', context)
