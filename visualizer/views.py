from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def most_viewed_creators(request):
    return render(request, 'most_viewed_creators.html', {'name': 'World'})
