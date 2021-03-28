from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')

    #check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    numberremover=request.POST.get('numberremover','off')

    #check which box is on
    if removepunc=="on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        print(djtext)
        return render(request,'analyze.html',params)

    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

        params={'purpose':'Changed To Upper Case','analyzed_text':analyzed}
        djtext=analyzed
        print(djtext)
        return render(request, 'analyze.html', params)

    if (extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if char==djtext[-1]:
                if not (djtext[index]==" "):
                    analyzed=analyzed + char

                elif not (djtext[index]==" " and djtext[index]==" "):
                    analyzed=analyzed + char

        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext=analyzed
        print(djtext)
        return render(request, 'analyze.html', params)

    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed + char
        params= {'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext=analyzed
        print(djtext)
        return render(request, 'analyze.html', params)

    if (numberremover=="on"):
        analyzed=""
        numbers='0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed= analyzed + char

        params={'purpose':'Removed Number','analyzed_text':analyzed}
        djtext=analyzed
        print(djtext)
        return render(request, 'analyze.html', params)

    if (removepunc !="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover !="on"):
        return HttpResponse("Please Select Any Operation And Try Again!..")

    return render(request,'analyze.html')

def about(request):
    return render(request, 'about.html')





        




