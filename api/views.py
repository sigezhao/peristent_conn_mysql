from django.shortcuts import render
from .models import *
import random
from django.http import HttpResponse

# create a function, get number of all rows in Riddle
def get_riddle_count(request):
    # write code to query number of all rows in Riddle, which row has enable equal False
    false_count = Riddle.objects.filter(enable=False).count()
    # write code to query row id, which has question like "大"
    riddle_with_question = Riddle.objects.filter(question__contains='大').count()
    riddle_count = Riddle.objects.all().count()
    # use false_count、riddle_with_question and riddle_count to compose a list, then random return one element.
    ret_list = [false_count, riddle_with_question, riddle_count]
    ret = random.choice(ret_list)
    
    return HttpResponse("Number of all rows in Riddle: " + str(ret))
