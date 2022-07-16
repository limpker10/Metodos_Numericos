from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def metodoBiseccion(request):
    if request.method == 'GET':
        return render(request,'biseccion.html')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        return render(request,'biseccion.html',{'name':nombre})
