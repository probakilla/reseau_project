#!/usr/bin/python3

from grid import *
import  random, socket, select, threading, sys

print ("Bienvenue dans le jeu du morpion aveugle.")
print ("Pour jouer il suffit de choisir une case de 0 à 8, les cases sont numérotees de la maniere suivante :")
print ("")
print ("     0 1 2 ")
print ("     3 4 5 ")
print ("     6 7 8 ")
print ("")

# connexion au serveur
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("", 1111))

case_number = input ('Choisissez une case a jouer : ')

sock.send (case_number.encode ())
grid = sock.recv (8192)

grid.display ()
