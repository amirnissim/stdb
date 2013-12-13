from django.shortcuts import render
from statements.models import Statement

def home(request):
  context = {'name': 'Yosef'}
  return render(request, 'index.html', context)