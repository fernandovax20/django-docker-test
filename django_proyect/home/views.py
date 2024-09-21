from django.shortcuts import render

def home_view(request):
    mensaje = "Hola mundo desde el backend"
    return render(request, 'home/home.html', {'mensaje': mensaje})
