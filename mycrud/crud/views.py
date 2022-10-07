
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def createEmpleado(request):
        codigo = request.POST['codigoInput']
        nit = request.POST['nitInput']
        nombre = request.POST['nombreInput']
        apellido1 = request.POST['apellido1Input']
        apellido2 = request.POST['apellido2Input']
        codigo_departamento = request.POST['codigo_departamento!']

   
   
        developer = Empleado.objects.create(
          codigo=codigo, nit=nit, nombre=nombre,apellido1=apellido1,apellido2=apellido2,codigo_departamento=codigo_departamento)
        messages.success(request, 'User: ' + codigo +' ¡Save Success !')
        return redirect('/')  
    
    

    
def listEmpleado(request):
            developers = Empleado.objects.all()
            return render(request, "index.html", {"developers": developers})


#------ Editar
def editEmpleado(request, slug):
    developer = Empleado.objects.get(slug=slug)

    codigo = request.POST.get['codigoInput']
    nit = request.POST.get['nitInput']
    nombre = request.POST.get['nombreInput']
    apellido1 = request.POST.get['apellido1Input']
    apellido2 = request.POST.get['apellido2Input']
    codigo_departamento = request.POST.get['codigo_departamento!']
    if request.method == 'POST':
        
        developer.codigo = codigo
        developer.nit = nit
        developer.nombre = nombre
        developer.apellido1 = apellido1
        developer.apellido2 = apellido2
        developer.código_departamento = codigo_departamento
        developer.save()
        messages.success(request, 'User: ' + codigo +' ¡Edit Success!')
        return redirect('/')

    return render (request, "edit.html", {"developer": developer})

# borrar 
def deleteEmpleado(request, slug):
    developer = Empleado.objects.get(slug=slug)

    developer.delete()
    messages.success(request, '¡Empleado Deleted!')
    return redirect('/')  