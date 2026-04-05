from django.shortcuts import render

# Create your views here.

def mainpage(request): 
    return render(request, 'main/mainpage.html')

def secondpage(request):
    context={
        'generation': 14,
        'info':{
            'name' : '최은서',
            'age' : '2006년 04월 12일',
            'number' : '010-9158-3643'
        }
    }
    return render(request, 'second/secondpage.html', context)