import argparse
#se uso parse para facilitar la escritura de las interfaces y sea un poco más fácil tomar argumentos para las clases
parser = argparse.ArgumentParser(description='Necesito')
parser.add_argument('-a','--alumnos', default=40,type=int, help='numero de alumnos')
parser.add_argument('-p','--profeso', default=10, type=int,help='numero de maestros')
#Argumentos
args= parser.parse_args()