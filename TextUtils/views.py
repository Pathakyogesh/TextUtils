
from django.http import HttpResponse
from django.shortcuts import render
def index(requests):
    return render(requests,"index.html")
def analyze(requests):
    text=requests.GET.get('Text','default')
    removepunc=requests.GET.get('removepunc','off')
    Uppercase=requests.GET.get('UPPERCASE','off')
    spaceremover=requests.GET.get('spaceremover','off')
    charcount = requests.GET.get('charactercount', 'off')
    newlineremover = requests.GET.get('newlineremover', 'off')
    analyzed = ""
    if(removepunc=='on'):
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in text:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(requests,'analyze.html',params)
    elif(Uppercase=='on'):
        for char in text:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        return render(requests, 'analyze.html', params)
    elif (spaceremover=='on'):
        for char in text:
            if(char!=' '):
                analyzed=analyzed+char
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}
        return render(requests, 'analyze.html', params)
    elif (newlineremover=='on'):
        for char in text:
            if(char!='\n'):
                analyzed=analyzed+char
        params = {'purpose': 'Removed newLine', 'analyzed_text': analyzed}
        return render(requests, 'analyze.html', params)
    elif (charcount=='on'):
        c=0;
        for char in text:
            c+=1;
        params = {'purpose': 'no. of character', 'analyzed_text': c}
        return render(requests, 'analyze.html', params)
    else:
        return HttpResponse("Error")
'''def newlineremover(requests):
    return HttpResponse("remove newline")
'''