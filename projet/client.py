#!/usr/bin/python3

from grid import *
import  random, socket, select, threading, sys

# connexion au serveur
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("", 1111))

