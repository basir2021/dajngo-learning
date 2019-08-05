#Custom Made file
from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
    return HttpResponse('Hello')

def temp(request):
    dict = {'name':'annonymousX129Z', 'place':'Constantinople'}
    return render(request,'index.html',dict)

def removepunc(request):
    text_rcvdd = request.POST.get('text','default')
    option = request.POST.get('removal','off')
    to_upper = request.POST.get('UPPERCASE','off')
    charCounter = request.POST.get('charCounter', 'off')
    removed ={'data':text_rcvdd}

    if option == 'on':
        removedPunctutation = ''.join([char for char in text_rcvdd if char not in string.punctuation ])
        removed= {'data':removedPunctutation}
    if to_upper =='on':
        removed = {'data':(''.join(removedPunctutation.split('\n'))).upper() }
        removed['data'] = ''.join(removed['data'].split('\r'))
    if charCounter == 'on':
        count = 0
        for i,val in  enumerate(text_rcvdd):
            if 91>ord(val)>64 or 123>ord(val)>96:
                count +=1
        removed['data'] += '\nThe number of character in the given string is \n' + str(count)

    return render(request,'newOne.html',removed)

def about(request):
    return HttpResponse('ABout')