from django.shortcuts import render

def index(request):
    variavel =("Olá, mundo!")
    frutas = ["abacate", "abacaxi", "uva"]
    return render(request, 'index.html', {'variavel': variavel, 'frutas': frutas})
