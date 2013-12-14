from django.shortcuts import render
from statements.models import Statement

def home(request):
  context = {'statements': Statement.objects.all()}
  return render(request, 'index.html', context)