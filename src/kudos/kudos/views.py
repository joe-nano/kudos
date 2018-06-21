import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from kudos.forms import KudoForm
from kudos.models import Kudo


def index(request):
  context = {
    'form': KudoForm(),
    'messages': []
  }
  if request.method == 'POST':
    form = KudoForm(request.POST)
    if form.is_valid():
      kudo = Kudo(from_person=form.cleaned_data['from_person'],
                  to_person=form.cleaned_data['to_person'],
                  text=form.cleaned_data['comment'],
                  created=datetime.datetime.now())
      kudo.save()
      context['messages'].append("Thank you for giving a Kudo")

  return render(request, 'upload.html', context)


def list_kudos(request):
  kudos = Kudo.objects.all()
  table = []
  for kudo in kudos:
    table.append([kudo.from_person, kudo.to_person, kudo.text])
  context = {
    'table': table
  }
  return render(request, 'show_table.html', context=context)
