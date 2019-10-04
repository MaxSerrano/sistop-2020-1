from threading import Semaphore
import threading, random
from arg import args
from profe import profesor,Materias,profesores

mutexP = [Semaphore(1) for i in range(args.profeso)]
listA = [Semaphore(0) for i in range(args.profeso)]
contadorA= 0
mutexC= Semaphore(1)

class Alumno(threading.Thread):
    def __init__(self,id):
        global contadorA
        threading.Thread.__init__(self)
        self.id = id
        self.materiaa = random.choice(Materias)
        

    def ProfesorAElegir(self,materiaa):
        
        for index,i in enumerate(profesores):
            if i.materia[0] ==  materiaa or i.materia[1] == materiaa or i.materia[2] == materiaa :
                return index
        return -1

    def RM(self):
        global contadorA
        mutexC.acquire()
        contadorA += 1
        mutexC.release()

        index = self.ProfesorAElegir(self.materiaa)
        if index == -1:
            print("Soy el Alumno %d y cursare %s " %(self.id,self.materiaa))
        else:
                mutexP[index].acquire()
                print("Soy el Alumno %d y cursare %s con el profesor %d" %(self.id,self.materi,profesores[index].id))
                profesores[index].contador += 1
                if profesores[index].contador == 10:
                    print("Inicia clase %d" %profesores[index].id)
                    profesores[index].contador = 0
                    for i in range(10):
                        listA[index].release()

                if contadorA == args.alumnos:
                    for  i in range(0, len(listA)):
                        for j in range(20):
                            listA[j].release()
                        if profesores[i].contador != 0:
                            print("El profesor %d le dara clase %d a el alumno" %(profesores[i].id,profesores[i].contador))

                mutexP[index].release()
                listA[index].acquire()

        if len(profesores) == 0:
            print("No hay profesor, ¡Rayos, no podre cursar las materias!")   
