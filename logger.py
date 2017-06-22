import log

archivoDeLog = None

def abrirArchivoLog():
    global archivoDeLog
    archivoDeLog = log.abrir("errores.txt")

def cerrarArchivoLog():
    global archivoDeLog
    log.cerrar(archivoDeLog)

def guardar(mensaje):
    global archivoDeLog
    log.guardar(archivoDeLog,mensaje)
