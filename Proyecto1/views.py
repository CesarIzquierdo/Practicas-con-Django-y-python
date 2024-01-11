from django.http import HttpResponse
import datetime
from django.template import Template,Context, loader
from django.shortcuts import render

class persona(object):
    def __init__(self, nombre, apellido):
        self.nombre =  nombre
        self.apellido = apellido


def saludo (request):  #primera vista
    p1 = persona("jefe cesar", "izquierdo")
    ahora = datetime.datetime.now()
    temas_del_curso = ["platillas", "modelos", "formularios", "despliegue"]
    #nombre = "cesar"
    #apellido = "Izquierdo"
    #doc_externo = loader.get_template('miplatilla.html')
    # forma de cargar sin open
    #doc_externo = open("C:/Users/cesar/OneDrive/Documentos/estudiar/1/Django/Proyecto1/Proyecto1/template/miplatilla.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close
    
    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})
    
    #documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})
    #return HttpResponse(documento)
    return render(request, "miplatilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})

def cursoC(request ):
    fechaActual = datetime.datetime.now()
    return render(request, "cursoC.html", {"dameFecha":fechaActual})

def cursoCss(request ):
    fechaActual = datetime.datetime.now()
    return render(request, "cursoCss.html", {"dameFecha":fechaActual})

def despedida(request):
    return HttpResponse("Hasta luego amigos de Django")

def dameFecha(request):
    fechaActual = datetime.datetime.now()
    
    documento = """<html>
        <body>
            <h1>
                Fecha y hora actuales %s
            </h1>
        </body>
    </html>"""  % fechaActual
    
    return HttpResponse(documento)


def calculaEdad(request, edad, anio):
    periodo = anio-2024
    edadFutura = edad+periodo
    
    documento = """<html>
        <body>
            <h2>
                En el año  %s tendrás %s años 
            </h2>
        </body>
    </html>"""  %(anio, edadFutura)
    
    return HttpResponse(documento)