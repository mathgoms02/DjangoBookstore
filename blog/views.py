from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('BLOG')
    return render(request, 
                  'blog/index.html')

def exemplo(request):
    print('exemplo')
    return render(request, 'blog/exemplo.html')

