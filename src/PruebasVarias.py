def creacionArchivo (numero):
    nombre = 'Jornada' + numero;
    fichero = open(nombre, 'wb')
    return fichero

def archivoJornadas(fichero1,texto):
    fichero1.write(texto + '\n')

def archivoClasificaciones(fichero1, texto):
    fichero1.write(texto + '\n')
