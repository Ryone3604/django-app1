from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title' : 'taitoru',
            'message' : 'de-da:',
            'form' : HelloForm()
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'anataha <b>' + request.POST['name'] + \
            '(' + request.POST['age'] + \
            ') </b>sann.<br>me-ruha <b>' + request.POST['mail'] + \
            '</b>desune.'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)


