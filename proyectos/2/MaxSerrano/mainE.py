from profe import profesor
from alum import Alumno
from arg import args

def inicioClase(alumno):
    print("Bienvenidos a clases")
    for j in range(0,alumno):
        a = Alumno(j)
        a.start()

def main():
    inicioClase(alumno=args.alumnos)
#llamando al main
if __name__ == '__main__': 
    main()
