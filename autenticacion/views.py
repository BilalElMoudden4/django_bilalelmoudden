from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Usuario
from .forms import LoginForm

# Vista de login sin sesión
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            contraseña = form.cleaned_data["contraseña"]
            try:
                usuario = Usuario.objects.get(email=email)
                if check_password(contraseña, usuario.contraseña):
                    # Guardamos de forma temporal el usuario (se eliminará al acceder a la home)
                    request.session["temp_usuario_id"] = usuario.id
                    messages.success(request, f"Bienvenido, {usuario.nombre}")
                    return redirect("home_no_session")
            except Usuario.DoesNotExist:
                pass
        messages.error(request, "Credenciales incorrectas")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# Vista de login con sesión
def login_session_view(request):
    if "usuario_id" in request.session:
        return redirect("home")  # Si ya tiene sesión, redirige a la home
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            contraseña = form.cleaned_data["contraseña"]
            try:
                usuario = Usuario.objects.get(email=email)
                if check_password(contraseña, usuario.contraseña):
                    request.session["usuario_id"] = usuario.id
                    messages.success(request, f"Bienvenido, {usuario.nombre}")
                    return redirect("home")
            except Usuario.DoesNotExist:
                pass
        messages.error(request, "Credenciales incorrectas")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# Vista de home para login con sesión
def home_view(request):
    usuario_id = request.session.get("usuario_id")
    usuario = Usuario.objects.filter(id=usuario_id).first()
    if usuario:
        return render(request, "home.html", {"usuario": usuario})
    messages.error(request, "Debes iniciar sesión para acceder.")
    return redirect("login")


# Vista de home para login sin sesión
def home_no_session_view(request):
    # Se extrae y elimina el ID temporal de la sesión
    usuario_id = request.session.pop("temp_usuario_id", None)
    if usuario_id:
        usuario = Usuario.objects.filter(id=usuario_id).first()
        if usuario:
            return render(request, "home.html", {"usuario": usuario})
    messages.error(request, "Debes iniciar sesión para acceder.")
    return redirect("login_no_session")


# Vista de logout
def logout_view(request):
    # Iterar sobre los mensajes existentes para vaciarlos
    list(messages.get_messages(request))
    
    # Eliminar cualquier dato de sesión relacionado con el login
    request.session.pop("usuario_id", None)
    request.session.pop("temp_usuario_id", None)
    
    # Agregar el mensaje de logout
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("login")