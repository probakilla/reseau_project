#!/usr/bin/python3

from grid import *
import  random, socket, select, threading, sys, time


nbClient = 0
class Client (threading.Thread) :

    def __init__ (self):

        threading.Thread.__init__ (self)
        self.nbClient = 0

    def run (self):
        while (self.nbClient < 2):
            time.sleep (1)
        gameOver = 0
        num = 1
        msg = str (num)
        J1.send(msg.encode ())
        num = 2
        msg = str (num)
        J2.send(msg.encode ())
        grids = grid()
        
        currentPlayer = 1
        grids.display ()
 
        while grids.gameOver() == -1:
            msg = str (gameOver)
            J1.send (msg.encode ())
            J2.send (msg.encode ())
            time.sleep(0.2)
            msg = str (currentPlayer)
            J1.send (msg.encode ())
            J2.send (msg.encode ())
            if (currentPlayer == 1) :
                case = J1.recv (8192)
                case = int (case)
                if (grids.cells[case] == EMPTY) :
                    grids.play (currentPlayer, case)
                    grids.display ()
                    msg = str (OK)
                    J1.send (msg.encode ())
                    time.sleep(0.2)
                    currentPlayer = currentPlayer%2+1
                elif (grids.cells[case] == currentPlayer):
                    msg = str (-1)
                    J1.send (msg.encode ())
                    time.sleep(0.2)
                else :    
                    msg = str (KO)
                    J1.send (msg.encode ())
                    time.sleep(0.2)
            else:
                case = J2.recv (8192)
                case = int (case)
                if (grids.cells[case] == EMPTY) :
                    grids.play (currentPlayer, case)
                    grids.display ()
                    msg = str (OK)
                    J2.send (msg.encode ())
                    time.sleep(0.2)
                    currentPlayer = currentPlayer%2+1
                elif (grids.cells[case] == currentPlayer):
                    msg = str (-1)
                    J2.send (msg.encode ())
                    time.sleep(0.2)
                else :    
                    msg = str (KO)
                    J2.send (msg.encode ())
                    time.sleep(0.2)
        print("game over")
        grids.display()
        gameOver = 1
        msg = str(gameOver)
        J1.send(msg.encode ())
        J2.send(msg.encode ())
        sock.close ()

    def setNbClient (self, nbClient) :
        self.nbClient = nbClient
              
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind (( '', 1111))
joueur = Client ()
joueur.start ()

sock.listen (1)
print ("Lancement du serveur.")

    # Connexion des joueurs 
while (nbClient != 2):
    socketClient = sock.accept ()
    nbClient += 1
    joueur.setNbClient (nbClient)
    if (nbClient == 1):
        J1 = socketClient[0]
    if (nbClient == 2):
        J2 = socketClient[0]
    
    
        
    

