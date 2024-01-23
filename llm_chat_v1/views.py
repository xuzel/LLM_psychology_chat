from django.shortcuts import render
from django.http import HttpResponse
from typing import List

Chat_Dict_list: List[dict] = []


def chat_main_view(request):
    return render(request, 'index.html')


