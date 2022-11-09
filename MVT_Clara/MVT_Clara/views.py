from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def fecha_actual(request):
    hoy=datetime.now().strftime("%d|%m|%Y")
    return HttpResponse(f"Fecha actual: {hoy}")


def datos_familiares(request):

    archivo = open(r'C:\Users\matia\OneDrive\Documentos\Coder\MVT_Clara\MVT_Clara\MVT_Clara\templates\mvt.html')

    #cramos el template y le pasamos el cont de archivo
    plantilla = Template(archivo.read())

    #cerramos archivo 
    archivo.close()

    informacion_nombre = ['Nombre: Lourdes M',
     'Nombre: Clara A.',
     'Nombre: Gustavo A.',
     'Nombre: Matias A.'
    ]

    informacion_edad = ['Edad: 46',
    'Edad: 18',
    'Edad: 50',
    'Edad: 20'
    ]

    datos = {'informacion': informacion_nombre,'Edad': informacion_edad}

    #creamos el contexto
    contexto = Context(datos)

    #creamos el doc

    documento = plantilla.render(contexto)

    return HttpResponse(documento)