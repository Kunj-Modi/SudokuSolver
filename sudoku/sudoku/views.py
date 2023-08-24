from django.http import HttpResponse
from django.template import loader
from .objects import *

def index(request):
    q_board = Question().question(35)
    s_board = FINAL_BOARD
    nums = list(range(10))
    template = loader.get_template('index.html')
    context = {"nums": nums, "puzzle": q_board, "solution": s_board}
    return HttpResponse(template.render(context, request))
