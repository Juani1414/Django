from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import EmailMessage
from .forms import FormularioContacto

# Create your views here.




def contacto(request):

    formulariocontacto=FormularioContacto()

    if request.method=="POST":
        formulariocontacto=FormularioContacto(data=request.POST)

        if formulariocontacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email_new=EmailMessage("Mensaje desde app django", 
            "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido),
            "",["arielleal2206@gmail.com"], reply_to=[email])

            try:

                email_new.send()

                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido") 


    return render(request, "contacto/contacto.html", { "formulario" : formulariocontacto})