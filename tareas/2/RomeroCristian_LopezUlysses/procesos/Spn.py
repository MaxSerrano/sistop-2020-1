#!/usr/bin/python3
# -*-coding: utf-8 -*-x

from math import ceil
from procesos.Planificar import Planificar


class Spn(Planificar):

    def __init__(self, quantum, proceso):
        Planificar.__init__(self, quantum, proceso)
  
    def procesos_vivos(self, procesos, total):
        temp_procesos = []
        for proceso in procesos:
            if proceso["llegada"] <= total and proceso["quantum"] > 0:
                if proceso["llegada"] == total:
                    proceso["inicio"] = total
                temp_procesos.append(proceso)
        return temp_procesos

    def start(self):
        # print(self.mostrar_procesos())
        texto = str()
        total = 0
        procesos_listos = []
        for proceso in self.proceso:
            proceso = {"nombre": proceso.nombre,
                       "t": ceil(proceso.t/self.quantum),
                       "quantum": ceil(proceso.t/self.quantum),
                       "llegada": proceso.llegada,
                       "inicio": -1,
                       "fin": 0}
            procesos_listos.append(proceso)
        procesos_terminados = []
        texto = ""

        while(len(procesos_listos) > 0):
            procesos_temp = []
            avant = False
            procesos_ejecucion = self.procesos_vivos(procesos_listos, total)
            procesos_ejecucion.sort(key=lambda x: x["t"], reverse=False)
            for proceso in procesos_listos:
                if proceso["quantum"] > 0:
                    if len(procesos_ejecucion) > 0:
                        if proceso == procesos_ejecucion[0]:
                            proceso["quantum"] = proceso["quantum"] - 1
                            total = total + 1
                            texto = texto + proceso["nombre"]
                            avant = True
                            if proceso["quantum"] == 0:
                                proceso["fin"] = total
                                procesos_terminados.append(proceso)
                    procesos_temp.append(proceso)
            if not avant:
                texto = texto + "| |"
                total = total + 1
            procesos_listos = procesos_temp
        for proceso in procesos_terminados:
            T = proceso["fin"] - proceso["llegada"]
            self.T_list.append(T)
            P = T/proceso["t"]
            self.P_list.append(P)
            R = proceso["t"]/T
            self.R_list.append(R)
            E = T - proceso["t"]
            self.E_list.append(E)

        promedios = self.promedios()
        print("SPN: T =", "{0:.2f}".format(promedios['T']),
              ", E =", "{0:.2f}".format(promedios['E']),
              ", P =", "{0:.2f}".format(promedios['P']))
        print(texto + '\n')
