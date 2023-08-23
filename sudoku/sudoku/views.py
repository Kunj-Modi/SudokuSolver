from django.http import HttpResponse
from django.template import loader
from .objects import *

def index(request):
    q_board = Question().question(35)
    nums = Board(q_board)
    template = loader.get_template('index.html')
    context = {'num':nums,}
    return HttpResponse(template.render(context, request))
