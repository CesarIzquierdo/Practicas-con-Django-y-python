from django.http import HttpResponse
import datetime
from django.template import Template,Context

class persona(object):
    def __init__(self, nombre, apellido):
        self.nombre =  nombre
        self.apellido = apellido


def saludo (request):  #primera vista
    p1 = persona("jefe cesar", "izquierdo")
    #nombre = "cesar"
    #apellido = "Izquierdo"
    ahora = datetime.datetime.now()
    temas_del_curso = ["platillas", "modelos", "formularios", "despliegue"]
    
    
    doc_externo = open("C:/Users/cesar/OneDrive/Documentos/estudiar/1/Django/Proyecto1/Proyecto1/template/miplatilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close
    
    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})
    
    documento = plt .render(ctx)
    return HttpResponse(documento)


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