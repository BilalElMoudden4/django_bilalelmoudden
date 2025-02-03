from django.shortcuts import redirect, render

# Create your views here.
def guardar_sesion(request):
    request.session['usuario'] = 'Juan'
    return render(request, guardar_sesion.html)

def recuperar_sesion(request):
    usuario = request.session('usuario', 'Invitado')
    return render(request, 'recuperar_sesion.html', {'usuario':usuario})

def eliminar_sesion(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    return redirect('recuperar-sesion')