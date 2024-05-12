from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title


def hello(request):
  bands = Band.objects.all()
  titles = Title.objects.all()
  return render(request, 'listings/hello.html',
                {'bands': bands})



def about(request):
  return HttpResponse('<h1>A propos de nous</h1> <p>Nous adorons Merch !</div>')
