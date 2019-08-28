#!/usr/bin/env python  

import sys, select, termios, tty

import math

import time
import os
#import rospkg


import socket




class local_server:
    def __init__(self):

        self.HOST = '192.168.208.153'
        self.PORT = 8001
        self.sock = socket.socket()
        #self.sock.connect((self.HOST, self.PORT))
        self.conn =None
        try:
            print ('Connectting ')
            self.sock.bind((self.HOST, self.PORT))
            self.sock.listen(10)
            #self.sock.connect(self.HOST, self.PORT)
            self.conn, self.addr = self.sock.accept()
            print ('Connected by ', self.addr)
            print ('Connected by ', self.conn)
        except :
            print("Connect faild.")
            sys.exit(0)


        self.local_x = 0
        self.local_y = 0


    def plocal(self,X,Y):
        print ("**********************************************")
        print ("value:")
        print ("local { x %s , y %s }" % (X,Y))
        time.sleep(0.1)

    def update(self):

        self.local_x = self.local_x+0.05
        self.local_y = self.local_y+0.05
        
        time.sleep(0.2)


    def transfer(self):
        sx = format((int)(self.local_x*10)).zfill(3)
        sy = format((int)(self.local_y*10)).zfill(3)
        tran = sx+" "+sy

        print(tran)

        message_to_send = tran.encode("UTF-8")
        self.conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
        self.conn.send(message_to_send)


        print ("**********************************************")
        #print("find local "+tran)
        #self.con.send(tran)
        #self.plocal([sx,sy])

if __name__ == '__main__':
    #srospy.init_node('tf_listener')
    up = local_server()
    while True:
        try:
            up.update()
            up.transfer()
        except :
            up.conn.close()
            up.sock.close()
        

    
    

