from django.shortcuts import render


def index(request):
    return render(request, 'menu/index.html')


def view_menu(request, menu_id):
    return render(request, 'menu/index.html')
