from django.shortcuts import render


# Create your views here.
def home(request):
    print('HOME') # aparecerá no terminal
    return render(request, 'home/index.html')

def pagina_inicial(request):
    print('Pagina Inicial')
    return render (request, 'home/pagina_inicial.html')