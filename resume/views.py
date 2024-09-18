from django.shortcuts import render
from .models import Person

def IndexView(request):
    person = Person.objects.prefetch_related('education', 'skills', 'experiences', 'projects').first()
    context = {'person': person}
    return render(request, 'resume/cv.html', context)
