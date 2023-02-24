
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get text
    dj_text = request.POST.get('text', 'default')

    # get check box value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover =request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    # for remove punctuation
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed =''

        for char in dj_text:
            if char not in punctuations:
                analyzed =analyzed+char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}    
        dj_text = analyzed

    # for case change
    if fullcaps == 'on':
        analyzed = ''

        for char in dj_text:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UPPERCASE', 'analyzed_text':analyzed}    
        dj_text = analyzed
    
    # extra apace remover
    
    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(dj_text):
            if not(dj_text[index] == " " and dj_text[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        dj_text = analyzed


    # remove new line
    if (newlineremover == "on"):
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

