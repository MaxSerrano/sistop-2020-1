import threading
import random
from arg import args

# Materias impartidas
Materias = ['Dispositivos de E/S','Circuitos electricos','Compiladores','Bases de datos','Redes de Datos','Criptografia','Sistemas de control','Automatas']

class profesor():
    contador = 0
    alumnos = []
    def __init__(self, id):
        self.id = id
        self.materia = random.sample(Materias,3)

        print("Soy el Profesor %d e imparto las materias de: %s, %s y %s" %(self.id,self.materia[0],self.materia[1],self.materia[2]))
 
profesores = []
for i in range(0,args.profeso):
    profesores.append(profesor(i))