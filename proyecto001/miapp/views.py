from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo,Autor
from django.contrib import messages
from miapp.forms import FormArticulo
# Create your views here.


def saludo(request):
    contexto= {"titulo": "SALUDO",
               "autor":"Hola"
    }
    return render(request, 'saludo.html', contexto)
def index(request):
    estudiantes = ['Isabella Caballero', 
                    'Alejandro Hermitaño',
                    'Joan Palomino',
                    'Pierre Bernaola']
    
    contexto=  {"mensaje":"enviando desde views",
                "titulo":"INICIO",
                "estudiantes": estudiantes}
    return render(request,'index.html', contexto)

def rango(request):
    if request.method =="POST":
        num1=1
        num2=2
        num1 =int(request.POST.get("num1"))
        num2 =int(request.POST.get("num2"))
        if num1>num2:
            num1, num2 = num2, num1
            #return redirect('rango',a=b, b=a)"otra forma de hacerlo"
        rango=range(num1,num2+1)
        contexto ={
            "titulo":"Rango de números",
            "a":num1,
            "b":num2,
            "rango_numeros": rango
        }
        return render(request, 'rango.html', contexto)
    return render(request, 'rango.html')
def save_autor(request):
    if request.method =='POST':
        nombre= request.POST['nombres']
        apellido= request.POST['apellidos']
        sexo= request.POST['sexo']
        fech_nacimiento= request.POST['fech_nacimiento']
        pais= request.POST['pais']
        autor = Autor(
             nombre=nombre,
             apellido= apellido,
             sexo= sexo,
             fech_nacimiento=fech_nacimiento,
             pais=pais
        )
        autor.save()
        return render(request, 'create_autor.html', {'mensaje': "Autor Guardado"})
    else:
        return render(request, 'create_autor.html', {'mensaje': "Autor no Guardado"})

def create_autor(request):
     return render(request, 'create_autor.html')

def save_articulo(request):
    mensajes={'titulo':"El titulo es demnasido corto",'contenido':"El contenido es muy corto"}
    
    if request.method =='POST':
        titulo = request.POST['titulo']
        contenido = request.POST['contenido']
        publicado = request.POST['publicado']
        error_contenido=False
        error_titulo=False
        if len(titulo) <= 5:
             error_titulo=True
        if len(contenido) <= 10:
             error_contenido=True
        if error_contenido or error_titulo:
             return render(request, 'create_articulo.html', {
                        'error_contenido':error_contenido,
                        'error_titulo':error_titulo,
                        'mensajes':mensajes,
                        'titulo': titulo,
                        'contenido': contenido,
                        'publicado': publicado
                    })            
        articulo = Articulo(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
        )
        articulo.save()
        return render(request, 'create_articulo.html', {'mensaje': "Articulo Guardado"})
    else:
        return HttpResponse("<h2>No se ha podido registrar el artículo</h2>")

def create_articulo(request):
    return render(request, 'create_articulo.html')

def buscar_articulo(request, id):
    try:
        #estamos buscando por id
            articulo = Articulo.objects.get(id=id)
            resultado = f"""Articulo: 
                                <br> <strong>ID:</strong> {articulo.id} 
                                <br> <strong>Título:</strong> {articulo.titulo} 
                                <br> <strong>Contenido:</strong> {articulo.contenido}
                                """
    except:
                resultado = "<h1> Artículo No Encontrado </h1>"

    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.titulo = "Enseñanza onLine en la UNTELS"
    articulo.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Articulo Editado: {articulo.titulo} - {articulo.contenido}")
def listar_articulos(request):
     articulos= Articulo.objects.all()
     return render(request, 'listar_articulos.html',{
        'articulos':articulos,
        'titulo': 'Listado de Artículos'
    })

def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')

def create_full_articulo(request):
    if request.method == 'POST':
        formulario = FormArticulo(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            # Hay 2 formas de recuperar la información
            titulo  = data_form.get('titulo')
            contenido = data_form['contenido']
            publicado = data_form['publicado']
            articulo = Articulo(
            titulo = titulo,
            contenido = contenido,
            publicado = publicado
            )
            articulo.save()
            # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
            messages.success(request, f'Se agregó correctamente el artículo {articulo.id}')

            return redirect('listar_articulos')
            #return HttpResponse(articulo.titulo + ' -  ' + articulo.contenido + ' - ' + str(articulo.publicado))
    else:
        #metodo get, se entra por primera vez a la pagina
        formulario = FormArticulo()
        # Generamos un formulario vacío

    return render(request, 'create_full_articulo.html',{'form':formulario})