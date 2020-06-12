from django.shortcuts import render


# Create your views here.
def home(request, idx1=0, idx2=0):
    return render(request, 'side_menu.html', {})